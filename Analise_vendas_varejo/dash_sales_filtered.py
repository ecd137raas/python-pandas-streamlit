import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(layout="wide")

df = st.session_state['data']

df['ID'] = range(1, len(df) + 1)
df = df.set_index(['ID'])

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
df['Mes'] = df['Mes'].replace(substituicoes)
customer=st.selectbox("Cliente", df["Cliente"].unique())
df=df[df["Cliente"] == customer]

#View
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

totais = df.groupby("Mes")["VlrPedido"].sum().reset_index()
totais = totais.sort_values('Mes')

fig_date = px.bar(df, x="Mes", y="VlrPedido", title="Faturamento por Mês")
col1.plotly_chart(fig_date)
fig_date = px.pie(df, values="VlrPedido", names="GateWayAtual", title="Gateway de Pagamento")
col2.plotly_chart(fig_date)
fig_date = px.pie(df, values="VlrPedido", names="StatusPagamento", title="Status de Pagamento")
col3.plotly_chart(fig_date)
fig_date = px.pie(df, values="VlrPedido", names="NomeFormaPagamento", title="Meio de Pagamento")
col4.plotly_chart(fig_date) 
