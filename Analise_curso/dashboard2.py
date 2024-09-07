import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df=pd.read_csv("vendas_carros.csv", sep=",", decimal="." ) #data frame
df["Data"]=pd.to_datetime(df["Data"]) #converter a data para datetime
df=df.sort_values("Data") #ordenar a coluna data

df["Marcas"] = df["Marca"] #criando um novo df chamado Mês
marca = st.sidebar.multiselect("Filtro por Marca", df["Marcas"].unique(), placeholder="Selecione a marca")
df_filtered= df[df["Marcas"] == marca]

col1, col2 = st.columns(2)

#marca vendida por filial
fig_date = px.bar(df_filtered, x="Data", y="Venda", color="Filial", title="Faturamento por dia")
col1.plotly_chart(fig_date)

fig_brand = px.bar(df_filtered, x="Venda", y="Marca", color="Filial", title="Faturamento por Marca", orientation="h")
col2.plotly_chart(fig_brand)

#city_total = df_filtered.groupby("Filial")[("Venda")].sum().reset_index()





