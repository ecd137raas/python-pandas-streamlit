import pandas as pd
from sqlalchemy import create_engine
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

server = os.getenv('SERVER')
database = os.getenv('DB')
username = os.getenv('USR')
password = os.getenv('PW')
connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server'
engine = create_engine(connection_string)

st.set_page_config(layout="wide")

# Escrever sua consulta SQL
order=st.text_input('Registro pedido')
query = f"select t.TenantAlias, p.CanalCriacaoId, p.DataCriacao, p.NumeroPedido, p.VRTOT, p.VRLIQ, p.VRDSC, p.Filial_Id, pg.ValorPagamento, g.NomeGateway, pg.TransactionId, sp.NomeStatusPedido, spo.NomeStatusPagamento, pg.AdditionalInfo from pedido p, pagamento pg, Tenant t, StatusPedido sp, StatusPagamento spo, GatewayPagamento g where p.TenantId=t.TenantId and p.id=pg.PedidoId and pg.GateWayPagamentoId=g.Id and p.StatusPedido_Id=sp.Id and pg.StatusPagamento_Id=spo.Id and p.REGISTROPEDIDO = '{order}'"

df = pd.read_sql(query, engine)


col1, col2 = st.columns(2)
if not df.empty:
    df["MeioPagamento"] = df.apply(lambda row: 'Pix' if 'PixDto' in row['AdditionalInfo'] else 'Cartão de Crédito' if 'Cartao' in row['AdditionalInfo'] else 'Boleto', axis=1)
    with col1:
        st.title("Dados do pedido ")
        st.text(f"Farmacia: {df['TenantAlias'].iloc[0]}", )
        st.text(f"Canal: {df['CanalCriacaoId'].iloc[0]}")
        st.text(f"Data: {df['DataCriacao'].iloc[0]}")
        st.text(f"Pedido: {df['NumeroPedido'].iloc[0]}")
        st.text(f"Filial: {df['Filial_Id'].iloc[0]}", help='Filial de origem do pedido')
        st.text(f"Status: {df['NomeStatusPedido'].iloc[0]}")
    with col2:
        st.title("Dados do pagamento ")
        st.text(f"Valor Liquido: {df['VRLIQ'].iloc[0]}")
        st.text(f"Valor Total: {df['VRTOT'].iloc[0]}")
        st.text(f"Desconto: {df['VRDSC'].iloc[0]}")
        st.text(f"Valor Pago: {df['ValorPagamento'].iloc[0]}")
        st.text(f"Gateway: {df['NomeGateway'].iloc[0]}")
        st.text(f"Transação: {df['TransactionId'].iloc[0]}")
        st.text(f"Meio de Pagamento: {df['MeioPagamento'].iloc[0]}")
        st.text(f"Status: {df['NomeStatusPagamento'].iloc[0]}")
        
else:
    st.warning('Dados de pedido ou pagamento não encontrados', icon="⚠️")


