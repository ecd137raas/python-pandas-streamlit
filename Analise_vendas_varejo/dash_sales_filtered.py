import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(layout="wide")

df= pd.read_csv("vendas.csv", sep=";", decimal=",", engine=None, encoding='utf-8')
df= df.sort_values(by='Mes')
df['ValorPedidoForm'] = df['Valor Pedido'].apply(lambda x: f'R${x:,.2f}'.replace(',', 'v').replace('.', ',').replace('v', '.'))

customer=st.selectbox("Cliente", df["Cliente"].unique())
df_range=df[df["Cliente"] == customer]

substituicoes = {
    1: 'Janeiro',
    2: 'Fevereiro',
    3: 'Março',
    4: 'Abril',
    5: 'Maio',
    6: 'Junho',
    7: 'Julho',
    8: 'Agosto',
    9: 'Setembro',
    10: 'Outubro',
    11: 'Novembro',
    12: 'Dezembro'
}
# Substituindo os valores na coluna 'Mes'
df_range['Mes'] = df_range['Mes'].replace(substituicoes)

df_range['Gateway Pagamento'] = df_range.apply(lambda row: 'Shipay' if 'PixDto' in row['Info'] else 'PagarMe' if 'PagarMe' in row['Info'] else row['Gateway Pagamento'], axis=1)
df_range["MeioPagamento"] = df_range.apply(lambda row: 'Pix' if 'PixDto' in row['Info'] else 'Crédito' if 'Cartao' in row['Info'] else 'Boleto', axis=1)
df_range["Bandeira"] = df_range.apply(lambda row: 'Visa' if 'visa' in row['Info'] else 'Visa' if 'Visa' in row['Info'] else 'Amex' if 'Amex' in row['Info'] else 'Amex' if 'amex' in row['Info'] else 'Master' if 'mastercard' in row['Info'] else 'Master' if 'Master' in row['Info'] else 'Elo' if 'elo' in row['Info'] else 'Elo' if 'Elo' in row['Info'] else 'Diners' if 'diners' in row['Info'] else 'Diners' if 'Diners' in row['Info'] else 'Pix/Boleto', axis=1)

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

totais = df_range.groupby("Mes")["Valor Pedido"].sum().reset_index()

fig_date = px.bar(totais, x="Mes", y="Valor Pedido", title="Faturamento por Mês")
col1.plotly_chart(fig_date)

fig_date = px.pie(df_range, values="Valor Pedido", names="Gateway Pagamento", title="Gateway de Pagamento")
col2.plotly_chart(fig_date)

fig_date = px.pie(df_range, values="Valor Pedido", names="Status Pagamento", title="Status de Pagamento")
col3.plotly_chart(fig_date)

fig_date = px.pie(df_range, values="Valor Pedido", names="MeioPagamento", title="Meio de Pagamento")
col4.plotly_chart(fig_date) 

fig_date = px.pie(df_range, values="Valor Pedido", names="Bandeira", title="Bandeira do Cartão")
col5.plotly_chart(fig_date)

df_range