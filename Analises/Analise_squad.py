import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_csv('DadosUS.csv', sep=';', engine=None, encoding='utf-8')
df = df.set_index('ID')
df['Tags'] = df['Tags'].fillna('erro')
df['Categoria'] = df.apply(lambda row: 'Débito Técnico' if '#Origem_Débito Técnico' in row['Tags'] else 'Melhorias' if '#Origem_Melhorias' in row['Tags'] else 'Bugs' if '#IgnorarMetrica' in row['Tags'] else 'Bugs' if '#BugInterno' in row['Tags'] else 'Nova Funcionalidade' if '#Origem_Nova Funcionalidade' in row['Tags'] else 'Sem Tag', axis=1)
df['Produto'] = df.apply(lambda row: 'Link de Pagamento' if 'Link de Pagamento' in row['Tags'] else 'WABA' if 'WABA' in row['Tags'] else 'Becaps' if 'Becaps' in row['Tags'] else 'Mobycenter' if 'Mobycenter' in row['Tags'] else 'Sem Tag', axis=1)

df

col1, col2, col3 = st.columns(3)

fig_date = px.bar(df, x="State", y="Categoria", color='Produto', title="Atuação por Categoria")
col1.plotly_chart(fig_date) 