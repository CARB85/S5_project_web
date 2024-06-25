import pandas as pd
import plotly.express as px
import streamlit as st

# Leer el archivo CSV
df = pd.read_csv(r'C:\Users\crist\Documents\Documentos\ds_my_projects\S5_project_web\vehicles_us.csv')

# Crear un encabezado
st.header('Análisis Exploratorio de Datos de Vehículos')

# Crear un botón para construir un histograma
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    st.write('Histograma segun el odometer')
    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Crear un botón para construir un gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter:
    st.write('Gráfico de dispersión precio vs odometer')
    fig = px.scatter(df, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
    