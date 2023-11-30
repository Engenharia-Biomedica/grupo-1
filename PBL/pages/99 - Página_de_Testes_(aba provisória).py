import pandas as pd
import streamlit as st
from PIL import Image



texto = st.text_input('Email') 
texto2 = st.text_input('Senha', type="password")

opcoes = ['Selecione uma opção', 'Camaleão', 'Cruzadas']

texto = st.selectbox('Escolha uma opção',opcoes)


img = Image.open('camaleao.png')



botao = st.button('Aplicar', type='primary')


    # Verifica o texto digitado pelo usuário e exibe o resultado correspondente
if botao:
    if texto.lower() == 'camaleão':
        st.image(img)
    elif texto.lower() == 'cruzadas':
        st.write('As Cruzadas foram uma série de expedições militares de caráter religioso organizadas pelos cristãos da Europa Ocidental com o objetivo de conquistar Jerusalém e os lugares sagrados do Cristianismo no Oriente Médio.')
    else:
        st.write(f'Você digitou: {texto}')



