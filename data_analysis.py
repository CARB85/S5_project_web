import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Análisis Exploratorio de Datos")

# Cargar datos
df = pd.read_csv(r'C:\Users\crist\Documents\Documentos\ds_my_projects\S5_project_web\vehicles_us.csv')

# Mostrar los datos
st.write(df.head())

# Crear una gráfica simple
fig = px.scatter(df, x='column_x', y='column_y')
st.plotly_chart(fig)
