import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide")
st.title("Indicadores da :blue[squad] :sunglasses:")

#Copie e cole do TFS em excel em branco, formate as datas para data simples, e formate a coluna ID para numero.
df = pd.read_csv('DadosUS.csv', sep=';')

#Tratamento dos dados
df=df.set_index('ID')
df['CT'] = 1 #range(1, len(df) + 1)
df['Tags'] = df['Tags'].fillna('Sem Tag')
df['Created Date'] = pd.to_datetime(df['Created Date'], format='%d/%m/%Y', errors='coerce')
df['Activated Date'] = pd.to_datetime(df['Activated Date'], format='%d/%m/%Y', errors='coerce')
df['Closed Date'] = pd.to_datetime(df['Closed Date'], format='%d/%m/%Y', errors='coerce')
df['Year']=df['Created Date'].dt.to_period('Y')
df['Month']=df['Created Date'].dt.to_period('M').astype(str)
df['Days']=(df['Closed Date'] - df['Activated Date']).dt.days
avg=df.groupby('Month')['Days'].mean().round(0).reset_index()

df['Category'] = df.apply(lambda row: 'Débito Técnico' if '#Origem_Débito Técnico' in row['Tags'] else 'Solicitação' if '#Origem_Solicitação' in row['Tags'] else 'Melhorias' if '#Origem_Melhorias' in row['Tags'] else 'Bugs' if '#IgnorarMetrica' in row['Tags'] else 'Bugs' if '#BugInterno' in row['Tags'] else 'Bugs' if '#Bug-Interno' in row['Tags'] else 'Nova Funcionalidade' if '#Origem_Nova Funcionalidade' in row['Tags'] else 'Sem Tag', axis=1)
df['Product'] = df.apply(lambda row: 'Link de Pagamento' if 'Link de Pagamento' in row['Tags'] else 'WABA' if 'WABA' in row['Tags'] else 'Becaps' if 'becaps' in row['Tags'] else 'Mobycenter' if 'Mobycenter' in row['Tags'] else 'Sem Tag', axis=1)
df['Support'] = df.apply(lambda row: 'Manut. Corretiva' if 'Manut Corretiva' in row['Tags'] else 'Manut. Evolutiva' if 'Manut Evolutiva' in row['Tags'] else 'Suporte' if 'Origem_Monitoramento' in row['Tags'] else 'Suporte' if 'Origem_Onboarding' in row['Tags'] else 'Suporte' if 'Origem_Suporte' in row['Tags'] else 'Suporte' if 'Expedite' in row['Tags'] else 'Sem Tag', axis=1)

#Relatórios
ds_years = st.selectbox("Filtro: Ano de referência", df["Year"].unique())
df_filtered= df[df["Year"] == ds_years]
ds_sup_filt = df_filtered[df_filtered['Support'] != 'Sem Tag']
ds_prd_filt = df_filtered[df_filtered['Product'] != 'Sem Tag']


col1, col2, col3 = st.columns(3)
col4, col5 = st.columns(2)

fig_date = px.pie(df_filtered, values='CT', names="Category", title="Categoria de Solicitação" )
col1.plotly_chart(fig_date) 
fig_date = px.pie(ds_sup_filt, values="CT", names="Support", title="Detalhando Solicitação/Bugs/DT")
col2.plotly_chart(fig_date) 
fig_date = px.pie(ds_prd_filt, values="CT", names="Product", title="Quantidade de registros por produto")
col3.plotly_chart(fig_date)
fig_date = px.pie(df_filtered, values="CT", names="State", title="Quantidade de registros por status")
col4.plotly_chart(fig_date)
fig_date = px.scatter(avg, x='Month', y='Days', title='Cycle time')
col5.plotly_chart(fig_date)


#Pendencias
# Criar a visão de Cicle tyme e Lead time da squad - done
# Melhorar a base com adição das tags para obter os filtros
