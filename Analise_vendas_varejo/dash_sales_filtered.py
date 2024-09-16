import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(layout="wide")

df= pd.read_csv("vendas.csv", sep=";", decimal=",", engine=None, encoding='utf-8')

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
df['Mes'] = df['Mes'].replace(substituicoes)
df['Mes'] = df['Mes'].astype('category')
df['Mes'].cat.set_categories(['Junho', 'Julho', 'Agosto', 'Setembro'])
df['ValorPedidoForm'] = df['Valor Pedido'].apply(lambda x: f'R${x:,.2f}'.replace(',', 'v').replace('.', ',').replace('v', '.'))


df['Gateway Pagamento'] = df.apply(lambda row: 'Shipay' if 'PixDto' in row['Info'] else 'PagarMe' if 'PagarMe' in row['Info'] else row['Gateway Pagamento'], axis=1)
df["MeioPagamento"] = df.apply(lambda row: 'Pix' if 'PixDto' in row['Info'] else 'Crédito' if 'Cartao' in row['Info'] else 'Boleto', axis=1)
df["Bandeira"] = df.apply(lambda row: 'Visa' if 'visa' in row['Info'] else 'Visa' if 'Visa' in row['Info'] else 'Amex' if 'Amex' in row['Info'] else 'Amex' if 'amex' in row['Info'] else 'Master' if 'mastercard' in row['Info'] else 'Master' if 'Master' in row['Info'] else 'Elo' if 'elo' in row['Info'] else 'Elo' if 'Elo' in row['Info'] else 'Diners' if 'diners' in row['Info'] else 'Diners' if 'Diners' in row['Info'] else 'Pix/Boleto', axis=1)

df.head()

# customer=st.selectbox("Cliente", df["Cliente"].unique())
# df=df[df["Cliente"] == customer]



#View

# col1, col2 = st.columns(2)
# col3, col4, col5 = st.columns(3)
# totais = df.groupby("Mes")["Valor Pedido"].sum().reset_index()
# fig_date = px.bar(totais, x="Mes", y="Valor Pedido", title="Faturamento por Mês")
# col1.plotly_chart(fig_date)
# fig_date = px.pie(df, values="Valor Pedido", names="Gateway Pagamento", title="Gateway de Pagamento")
# col2.plotly_chart(fig_date)
# fig_date = px.pie(df, values="Valor Pedido", names="Status Pagamento", title="Status de Pagamento")
# col3.plotly_chart(fig_date)
# fig_date = px.pie(df, values="Valor Pedido", names="MeioPagamento", title="Meio de Pagamento")
# col4.plotly_chart(fig_date) 
# fig_date = px.pie(df, values="Valor Pedido", names="Bandeira", title="Bandeira do Cartão")
# col5.plotly_chart(fig_date)