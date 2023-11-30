import pandas as pd
import streamlit as st
from PIL import Image

# Header
st.header("Painel Interativo de Antibióticos e Bactérias")

# carregando imagem para o logo
img = Image.open("celulas.png")


# dividindo o espaçamento da tela em colunas
col_esquerda, col_central, col_direita = st.columns(3)


# colocando o logo na coluna central
with col_esquerda:
    st.image(img, width=800)

# Texto introdutório
st.markdown("Métricas importantes relacionadas a resistência de agentes patogênicos a Antibióticos.")




