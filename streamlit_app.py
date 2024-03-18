# Importando bibliotecas
import pandas as pd
import streamlit as st
import plotly.express as px

# Importando os dados que estao em parquet
dados = pd.read_parquet('/content/drive/MyDrive/PySUS/ANIMBR07_22.parquet.gzip')

st.dataframe(dados)
