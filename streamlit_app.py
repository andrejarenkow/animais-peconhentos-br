# Importando bibliotecas
import pandas as pd
import streamlit as st
import plotly.express as px


@st.cache_data
def load_data(persist=True):
  # Importando os dados que estao em parquet
    data = pd.read_parquet('https://drive.google.com/uc?export=download&id=1-4ZSiWudlwmC0kCHDCX46qPp5RGNwT4X')
    return data


dados = load_data()



