import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np
#import util as ut

st.set_page_config(layout="wide")

#Copie e cole do TFS em excel em branco, formate as datas para data simples, e formate a coluna ID para numero.
df = pd.read_csv('DadosUS.csv', sep=';')

#Tratamento dos dados
df['Tags'] = df['Tags'].fillna('Sem Tag')
df['Created Date'] = pd.to_datetime(df['Created Date'], format='%d/%m/%Y', errors='coerce')
df['Activated Date'] = pd.to_datetime(df['Activated Date'], format='%d/%m/%Y', errors='coerce')
df['Closed Date'] = pd.to_datetime(df['Closed Date'], format='%d/%m/%Y', errors='coerce')
df['Year']=df['Created Date'].dt.to_period('Y')
df['Month']=df['Created Date'].dt.month.astype(str).str.zfill(2)
df['Days']=(df['Closed Date'] - df['Activated Date']).dt.days

df['Category'] = df.apply(lambda row: 'Débito Técnico' if '#Origem_Débito Técnico' in row['Tags'] else 'Solicitação' if '#Origem_Solicitação' in row['Tags'] else 'Melhorias' if '#Origem_Melhorias' in row['Tags'] else 'Bugs' if '#IgnorarMetrica' in row['Tags'] else 'Bugs' if '#BugInterno' in row['Tags'] else 'Bugs' if '#Bug-Interno' in row['Tags'] else 'Nova Funcionalidade' if '#Origem_Nova Funcionalidade' in row['Tags'] else 'Sem Tag', axis=1)
df['Product'] = df.apply(lambda row: 'Link de Pagamento' if 'Link de Pagamento' in row['Tags'] else 'WABA' if 'WABA' in row['Tags'] else 'Becaps' if 'becaps' in row['Tags'] else 'Mobycenter' if 'Mobycenter' in row['Tags'] else 'Sem Tag', axis=1)
df['Support'] = df.apply(lambda row: 'Manut. Corretiva' if 'Manut Corretiva' in row['Tags'] else 'Manut. Evolutiva' if 'Manut Evolutiva' in row['Tags'] else 'Suporte' if 'Origem_Monitoramento' in row['Tags'] else 'Suporte' if 'Origem_Onboarding' in row['Tags'] else 'Suporte' if 'Origem_Suporte' in row['Tags'] else 'Suporte' if 'Expedite' in row['Tags'] else 'Sem Tag', axis=1)

#Relatórios
years = st.sidebar.selectbox("Ano", df["Year"].unique())
df_filtered= df[df["Year"] == years]
df['ID']=df['ID'].value_counts()
df_cat_filt = df_filtered[df_filtered['Category'] == 'Sem Tag']

col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)

fig_date = px.pie(df_filtered, values="ID", names="Category", title="Tipo de Solicitação" )
col1.plotly_chart(fig_date) 
fig_date = px.pie(df_filtered, values="ID", names="Support", title="Atuação com Suporte")
col2.plotly_chart(fig_date) 
fig_date = px.pie(df_filtered, values="ID", names="Product", title="Quantidade de registros por produto")
col3.plotly_chart(fig_date)
fig_date = px.pie(df_filtered, values="ID", names="State", title="Quantidade de registros por status")
col4.plotly_chart(fig_date) 

df_filtered
#df_cat_filt

#Pendencias
# Criar a visão de Cicle tyme e Lead time da squad 
# Melhorar a base com adição das tags para obter os filtros