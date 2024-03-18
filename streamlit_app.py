# Importando bibliotecas
import pandas as pd
import streamlit as st
import plotly.express as px

# Configurando a página

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Importação de dados
@st.cache_data
def load_data(persist=True):
  # Importando os dados que estao em parquet
    data = pd.read_parquet('https://drive.google.com/uc?export=download&id=1-79XeKun6Eqnxl6C_km5BgIG-XF2gW8h')
    return data


dados = load_data()

acidentes_serie_historica = pd.pivot_table(dados, index='Data do acidente', aggfunc='size').reset_index(name='Acidentes')

fig = px.line(acidentes_serie_historica, x="Data do acidente", y="Acidentes", title='Acidentes por animais peçonhentos, BR, 2019 a 2022')
st.plotly_chart(fig)
