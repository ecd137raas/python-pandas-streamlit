import streamlit as st

def home():
    st.title("Home Page")

pg = st.navigation([
    st.Page(home, title="Home Page", icon=":material/home:"),
    st.Page("dash_sales.py", title="Dados Gerais", icon=":material/favorite:"),
    st.Page("dash_sales_filtered.py", title="Dados por Clientes", icon=":material/cloud:"),
    st.Page("order_filter.py", title="Dados do Pedido", icon=":material/search:"),
])
pg.run()