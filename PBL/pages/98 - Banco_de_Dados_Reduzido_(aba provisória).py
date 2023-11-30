import pandas as pd
import streamlit as st


st.header("Variáveis Selecionadas para Manipulação") #Título da página Tabelas

dados = pd.read_csv('sample_data_clean.csv', sep = ',') #Leitura do CSV com pandas


    # Colunas G, J, P, Z, AB, AC, AD, AE viram índices do python (Ex. A é 0; B é 1; ...)
colunas_selecionadas = [6, 9, 15, 25, 27, 28, 29, 30, 32]  
dados_selecionados = dados.iloc[:, colunas_selecionadas]


st.dataframe(dados_selecionados) # Exibição do dataframe (dados)

