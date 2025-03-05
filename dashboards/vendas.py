import streamlit as st
import pandas as pd
import plotly.express as px

# Título do Dashboard
st.title("Dashboard de Análise de Vendas")

# Carregar dados
@st.cache_data
def carregar_dados():
    return pd.read_csv("data/vendas.csv")  # Substitua pelo seu arquivo CSV
df = carregar_dados()

# Filtro por categoria
categorias = df["Categoria"].unique()
categoria_selecionada = st.selectbox("Selecione uma categoria", categorias)

# Filtrar dados
df_filtrado = df[df["Categoria"] == categoria_selecionada]

# Exibir tabela
st.write("Dados Filtrados:")
st.dataframe(df_filtrado)

# Gráfico de barras (Vendas por Produto)
st.subheader("Vendas por Produto")
fig = px.bar(df_filtrado, x="Produto", y="Vendas", color="Produto", title="Vendas por Produto")
st.plotly_chart(fig)

# Gráfico de pizza (Distribuição de Vendas por Categoria)
st.subheader("Distribuição de Vendas por Categoria")
fig2 = px.pie(df, names="Categoria", values="Vendas", title="Distribuição de Vendas")
st.plotly_chart(fig2)