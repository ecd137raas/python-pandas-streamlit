import streamlit as st

def home():
    st.title("Home Page")

pg = st.navigation([
    st.Page(home, title="Home Page", icon="🔥"),
    st.Page("dash_vendas.py", title="Dados Gerais", icon=":material/favorite:"),
    st.Page("dash_vendas_filtro.py", title="Dados por Clientes", icon=":material/cloud:"),
])
pg.run()