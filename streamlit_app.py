# Importando bibliotecas
import pandas as pd
import streamlit as st
import plotly.express as px


@st.cache_data
def load_data(persist=True):
  # Importando os dados que estao em parquet
    data = pd.read_parquet('https://drive.google.com/uc?export=download&id=1-79XeKun6Eqnxl6C_km5BgIG-XF2gW8h')
    return data


dados = pd.read_parquet('https://drive.google.com/uc?export=download&id=1-79XeKun6Eqnxl6C_km5BgIG-XF2gW8h')



