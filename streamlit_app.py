import streamlit as st
import pandas as pd

st.title("Meu primeiro app de dados")

dados = pd.DataFrame({
    "Fruta": ["Maçã", "Banana", "Laranja"],
    "Vendas": [12, 19, 8],
})

st.write("Uma tabela simples:")
st.dataframe(dados)

st.bar_chart(dados.set_index("Fruta"))