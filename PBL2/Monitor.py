import streamlit as st
import hydralit_components as hc
import pandas as pd
import plotly.express as px
import pydeck as pdk
import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster

from monitor_components import *

st.set_page_config(layout='wide', initial_sidebar_state='collapsed')

logo_einstein = 'logo_einstein.jpg'
predio_einstein = 'predio_einstein.jpg'



col1, col2, col3 = st.columns([0.5,10,2])

with col2:
    st.header('')
    st.title('Painel de Monitoramento de Bactérias')
    st.header('')

with col3:
    st.header('')
    st.image(logo_einstein)#, width=400)


# specify the primary menu definition
menu_data = [
    {'icon': "fas fa-home", 'label': "Home"},
    {'icon': "fas fa-table", 'label': "Tabelas"},
    {
        'icon': "far fa-chart-bar",
        'label': "Gráficos",
        'submenu': [
            {'id': 'subid11', 'icon': "fa fa-paperclip", 'label': "Evolução do Antibiograma para uma Bactéria no Decorrer dos Anos"},
            {'id': 'subid12', 'icon': "fa fa-paperclip", 'label': "AntibiogramaXAntibiótico"}
        ]
    },
    {'icon': "fas fa-map", 'label': "Mapa da Rede"}
]

over_theme = {'txc_inactive': '#FFFFFF'}

menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    #login_name='Logout',  # Logout ainda é um link, não um botão de encerramento
    hide_streamlit_markers=True, 
    sticky_nav=True, 
    sticky_mode='pinned', 
)


# Adicionando a mensagem de boas-vindas na Home
if menu_id == 'Home':
    col1, col2, col3 = st.columns([1,20,20])
    
    with col2:
        st.header('', divider='blue') 
        st.title('Sobre o Projeto:') 
        st.subheader('Painel de monitoramento voltado para a facilitação das tomadas de decisões sobre o uso de antibióticos para o combate de microrganismos, avaliando a resistência desses contra os fármacos no decorrer dos anos.')
        st.header('', divider='blue') 

        #st.header('', divider='blue') 
        st.header('E-mail para contato:') 
        st.subheader('email@decontato.com.br')
        st.header('', divider='blue') 
    with col3:
        st.image(predio_einstein)
   


# Placeholder para ação de logout (não fecha o servidor Streamlit)
if menu_id == 'Tabelas':
    col1, col2, col3 = st.columns([10,1,10])
    with col1:
        exibir_df_dados()
        exibir_df_mesclado()
        exibir_df_dados_selecionados()
        
    with col3:
        exibir_df_unidade_bac()
        exibir_df_antibiotico_bac()


# Primeira subdivisão dos gráficos
if menu_id == 'subid11':
    exibir_grafico_antibiograma_bac('scatter')
    

# Segunda subdivisão dos gráficos    
if menu_id == 'subid12':
    exibir_grafico_antibiograma_bac('bar')


if menu_id == 'Mapa da Rede':
    exibir_mapa_unidade_bac()
    #exibir_df_unidade_bac()
        
    
