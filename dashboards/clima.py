import streamlit as st
import pandas as pd
import plotly.express as px

# Título do Dashboard
st.title("Dashboard de Análise Climática")

# Carregar dados
@st.cache_data
def carregar_dados():
    return pd.read_csv("data/clima.csv")  # Substitua pelo seu arquivo CSV
df = carregar_dados()

# Filtro por cidade
cidades = df["Cidade"].unique()
cidade_selecionada = st.selectbox("Selecione uma cidade", cidades)

# Filtrar dados
df_filtrado = df[df["Cidade"] == cidade_selecionada]

# Ordenar dados por data
df_filtrado = df_filtrado.sort_values(by="Data")

# Gráfico de linhas (Temperatura ao Longo do Tempo)
st.subheader("Temperatura ao Longo do Tempo")
fig = px.line(df_filtrado, x="Data", y="Temperatura", title=f"Temperatura em {cidade_selecionada}")
st.plotly_chart(fig)

# Gráfico de barras (Precipitação Mensal)
st.subheader("Precipitação Mensal")
fig2 = px.bar(df_filtrado, x="Data", y="Precipitação", title=f"Precipitação em {cidade_selecionada}")
st.plotly_chart(fig2)