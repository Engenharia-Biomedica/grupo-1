import streamlit as st
import pandas as pd
import numpy as np



########################## def FiltrarDados()

dados = pd.read_csv('sample_data_clean.csv', sep = ',') #Leitura do CSV com pandas


    # Colunas G, J, P, Z, AB, AC, AD, AE viram índices do python (Ex. A é 0; B é 1; ...)
colunas_selecionadas = [6, 9, 15, 25, 27, 28, 29, 30] 

dados_selecionados = dados.iloc[:, colunas_selecionadas]

# df é a sinônimo de "DataFrame"!
df = dados_selecionados

# Tipo de Exame (6)
# Sigla do Exame (9)
# Unidade de Coleta (15)
# Material de Coleta (Secreção, Urina, etc.) (25)
# Sigla do Microorganismo (27)
# Nome do Microorganismo (28)
# Sigla do Antibiótico (29)
# Nome do Antibiótico (30)




########################## def ExibirDados()

# Tabela Bactéria x Antibiótico (Índice 28 e 30)

# Definindo as colunas de Microorganismo e Antibiótico
# Substitua 'Microorganismo' e 'Antibiotico' pelos nomes reais das colunas no seu DataFrame
coluna_microorganismo = 'ds_micro_organismo'                # Substitua pelo nome real da coluna no seu DataFrame
coluna_antibiotico = 'ds_antibiotico_microorganismo'        # Substitua pelo nome real da coluna no seu DataFrame

# Agrupar por Microorganismo e Antibiótico e contar as ocorrências
microorganismo_vs_antibiotico = df.groupby([coluna_microorganismo, coluna_antibiotico]).size().reset_index(name='Quantidade')
resultado = microorganismo_vs_antibiotico

# Exibir o DataFrame resultante no Streamlit
st.title('Frequência de Microorganismos e Antibióticos')
st.dataframe(resultado)

