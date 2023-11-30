import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px

# Carregamento de dados
dados = pd.read_csv('sample_data_clean.csv', sep=',')


    # Colunas G, J, P, Z, AB, AC, AD, AE viram índices do python (Ex. A é 0; B é 1; ...)
colunas_selecionadas = [6, 9, 15, 25, 27, 28, 29, 30, 32] 

dados_selecionados = dados.iloc[:, colunas_selecionadas]

# df é a sinônimo de "DataFrame"!
df = dados_selecionados










########################## def ExibirDados()

# Tabela Bactéria x Antibiótico (Índice 28 e 30)

# Definindo as colunas de Microorganismo e Antibiótico
coluna_microorganismo = 'ds_micro_organismo'
coluna_antibiotico = 'ds_antibiotico_microorganismo'

# Agrupar por Microorganismo e Antibiótico e contar as ocorrências
microorganismo_vs_antibiotico = df.groupby([coluna_microorganismo, coluna_antibiotico]).size().reset_index(name='Quantidade')
resultado = microorganismo_vs_antibiotico

# Exibir o DataFrame resultante no Streamlit
st.title('Frequência de Microorganismos e Antibióticos')
st.dataframe(resultado)
db = resultado









# Processamento dos dados
df['Sensivel'] = np.where(df['cd_interpretacao_antibiograma'] == 'Sensível', 'Sensível', None)
df['Sensivel_Aumentando_Exposicao'] = np.where(df['cd_interpretacao_antibiograma'] == 'Sensível Aumentando Exposição', 'Sensível Aumentando Exposição', None)
df['Resistente'] = np.where(df['cd_interpretacao_antibiograma'] == 'Resistente', 'Resistente', None)

# Exibir o DataFrame no Streamlit
st.title('Visualização dos Dados com as Colunas de Resultados Separadas')
st.dataframe(df)



























# Agrupar e contar os dados
resultado_agrupado = dados.groupby(['ds_micro_organismo', 'ds_antibiotico_microorganismo', 'cd_interpretacao_antibiograma']).size().reset_index(name='Quantidade')

# Criar a SelectBox para escolher o Antibiótico
antibiotico_escolhido = st.selectbox('Escolha um Antibiótico', dados['ds_antibiotico_microorganismo'].unique())

# Filtrar o DataFrame com base no Antibiótico escolhido
df_filtrado = resultado_agrupado[resultado_agrupado['ds_antibiotico_microorganismo'] == antibiotico_escolhido]

# Criar o Gráfico
plt.figure(figsize=(10, 6))
sns.barplot(data=df_filtrado, x='ds_micro_organismo', y='Quantidade', hue='cd_interpretacao_antibiograma')
plt.xticks(rotation=45)
plt.xlabel('Microorganismo')
plt.ylabel('Frequência')
plt.title(f'Frequência de Categorias para o Antibiótico {antibiotico_escolhido}')

# Exibir o gráfico no Streamlit
st.pyplot(plt)








resultado_agrupado2 = df.groupby(['ds_micro_organismo', 'ds_antibiotico_microorganismo', 'cd_interpretacao_antibiograma']).size().reset_index(name='Quantidade')

# Criar a SelectBox para escolher o Antibiótico
antibiotico_escolhido = st.selectbox('Escolha um Antibiótico Rapaz', df['ds_antibiotico_microorganismo'].unique())

# Filtrar o DataFrame com base no Antibiótico escolhido
df_filtrado = resultado_agrupado2[resultado_agrupado2['ds_antibiotico_microorganismo'] == antibiotico_escolhido]

# Criar o Gráfico com Plotly
fig = px.bar(df_filtrado, x='ds_micro_organismo', y='Quantidade', color='cd_interpretacao_antibiograma',
             title=f'Frequência de Categorias para o Antibiótico {antibiotico_escolhido}')

# Exibir o gráfico no Streamlit
st.plotly_chart(fig)

