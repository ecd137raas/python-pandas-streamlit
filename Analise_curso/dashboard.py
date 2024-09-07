import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df=pd.read_csv("vendas_carros.csv", sep=",", decimal="." )
df["Data"]=pd.to_datetime(df["Data"])
df=df.sort_values("Data")

df["Month"] = df["Data"].apply(lambda x: str(x.month) + "-" + str(x.year))
month = st.sidebar.selectbox("Filtro Mês - Ano", df["Month"].unique())
df_filtered= df[df["Month"] == month]

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

fig_date = px.bar(df_filtered, x="Data", y="Venda", color="Filial", title="Faturamento por dia")
col1.plotly_chart(fig_date)

fig_brand = px.bar(df_filtered, x="Venda", y="Marca", color="Filial", title="Faturamento por Marca", orientation="h")
col2.plotly_chart(fig_brand)

city_total = df_filtered.groupby("Filial")[("Venda")].sum().reset_index()

fig_fil = px.bar(city_total, x="Filial", y="Venda", title="Faturamento por Filial")
col3.plotly_chart(fig_fil)

fig_type = px.pie(df_filtered, values="Venda", names="Tipo_Pagamento", title="Faturamento por Tipo de Pagamento")
col4.plotly_chart(fig_type)



