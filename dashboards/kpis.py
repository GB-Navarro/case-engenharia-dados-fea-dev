import streamlit as st
import pandas as pd
import plotly.express as px

# Título do Dashboard
st.title("Dashboard de Monitoramento de KPIs")

# Carregar dados
@st.cache_data
def carregar_dados():
    return pd.read_csv("data/kpis.csv")  # Substitua pelo seu arquivo CSV
df = carregar_dados()

# Exibir KPIs
st.subheader("KPIs Principais")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Vendas Totais", f"R$ {df['Vendas'].sum():,.2f}")
with col2:
    st.metric("Lucro Total", f"R$ {df['Lucro'].sum():,.2f}")
with col3:
    st.metric("Custo Total", f"R$ {df['Custo'].sum():,.2f}")

# Gráfico de linhas (Vendas ao Longo do Tempo)
st.subheader("Vendas ao Longo do Tempo")
fig = px.line(df, x="Data", y="Vendas", title="Vendas Mensais")
st.plotly_chart(fig)

# Gráfico de barras (Lucro por Produto)
st.subheader("Lucro por Produto")
fig2 = px.bar(df, x="Produto", y="Lucro", color="Produto", title="Lucro por Produto")
st.plotly_chart(fig2)