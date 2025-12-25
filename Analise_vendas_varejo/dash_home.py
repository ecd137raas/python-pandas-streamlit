import streamlit as st
import pandas as pd

def home():
    st.title("Home Page")

df = pd.read_csv("./Dados/consolidado25.csv")
st.session_state['data'] = df

pg = st.navigation([
    st.Page(home, title="Home Page", icon=":material/home:"),
    st.Page("dash_sales.py", title="Dados Gerais", icon=":material/favorite:"),
    st.Page("dash_sales_filtered.py", title="Dados por Clientes", icon=":material/cloud:"),
])
pg.run()