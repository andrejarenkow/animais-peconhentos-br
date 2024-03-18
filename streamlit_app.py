# Importando bibliotecas
import pandas as pd
import geopandas as gpd
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go
import requests
import folium
from streamlit_folium import st_folium, folium_static
import requests
import json
from datetime import datetime
import urllib.parse
import urllib.request
import re

# Configurando a página

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Importação shape estados Brasil
with urllib.request.urlopen("https://raw.githubusercontent.com/giuliano-macedo/geodata-br-states/main/geojson/br_states.json") as url:
  brasil_states = json.loads(url.read().decode())

# Mapa
# Criar um objeto de mapa
mapa = folium.Map(location=[-12.77314489018321, -50.30787352375238], zoom_start=3)

# Criando o pop up
popup = folium.GeoJsonPopup(
    fields=["Estado"],
    localize=True,
)

# Adicionando as CRS
folium.GeoJson(brasil_states,
               style_function=lambda feature: {
                "fillColor": 'black',
                "color": "grey",
                "weight": 0.8,
               'fillOpacity':0},
               highlight_function=lambda feature: {
                "fillColor": 'red',
                "color": "black",
                "weight": 3,
               'fillOpacity':0.6
                },
               popup=popup,
               popup_keep_highlighted=True,
               ).add_to(mapa)

# Importação de dados
@st.cache_data
def load_data(persist=True):
  # Importando os dados que estao em parquet
    data = pd.read_parquet('https://drive.google.com/uc?export=download&id=1-79XeKun6Eqnxl6C_km5BgIG-XF2gW8h')
    return data

dados = load_data()
#############################################
coluna_grafico, coluna_mapa = st.columns(2)
with coluna_mapa:
    # Exibindo o Mapa
    st_data = st_folium(mapa, width=600, height=800)
    st.write(st_data)

#Filtrando de acordo com o mapa
try:
    estado_filtro = st_data['last_active_drawing']['properties']['SIGLA'] #last active drawing vai direto para o ultimo clicado

    dados_filtrado = dados[dados['UF do acidente']==estado_filtro]
except:
    estado_filtro = 'BR'
    dados_filtrado = dados
    
acidentes_serie_historica = pd.pivot_table(dados_filtrado, index='Data do acidente', aggfunc='size').reset_index(name='Acidentes')

fig = px.line(acidentes_serie_historica, x="Data do acidente", y="Acidentes", title=f'Acidentes por animais peçonhentos, {estado_filtro}, 2019 a 2022')
with coluna_grafico:
    st.plotly_chart(fig, use_container_width=True)

