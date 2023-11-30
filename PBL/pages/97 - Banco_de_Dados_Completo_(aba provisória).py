import pandas as pd
import streamlit as st


st.header("Banco de Dados Completo com todas as variáveis") #Título da página Tabelas

dados = pd.read_csv('sample_data_clean.csv', sep = ',') #Leitura do CSV com pandas

st.dataframe(dados) # Exibição do dataframe (dados)

