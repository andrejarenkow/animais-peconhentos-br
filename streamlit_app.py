# Importando bibliotecas
import pandas as pd
import streamlit as st
import plotly.express as px

# Importando os dados que estao em parquet
dados = pd.read_parquet('https://drive.google.com/uc?export=download&id=1Fp0ndVsc49aZB1LhuKL0ivZ1PY2592GN')

st.dataframe(dados)
