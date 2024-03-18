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
mapa = folium.Map(location=[-30.510000000000, -53.8000000000], zoom_start=6)

# Adicionando as CRS
folium.GeoJson(brasil_states,
               style_function=lambda feature: {
                "fillColor": 'black',
                "color": "grey",
                "weight": 0.8,
               'fillOpacity':0},
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
    st_data = st_folium(mapa, width=500, height=450)

#Filtrando de acordo com o mapa
#filtro = 

acidentes_serie_historica = pd.pivot_table(dados, index='Data do acidente', aggfunc='size').reset_index(name='Acidentes')

fig = px.line(acidentes_serie_historica, x="Data do acidente", y="Acidentes", title='Acidentes por animais peçonhentos, BR, 2019 a 2022')
with coluna_grafico:
    st.plotly_chart(fig, use_container_width=True)
