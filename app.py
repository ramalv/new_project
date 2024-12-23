import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Análisis de Datos de Vehículos')

# Leer los datos
data = pd.read_csv('notebooks/vehicles_us.csv')

# Manejo de valores nulos en model_year
data = data.dropna(subset=['model_year'])

# Mostrar los datos
st.header('Datos de Vehículos')
st.write(data.head())

# Histograma del odómetro
if st.checkbox('Mostrar histograma del odómetro'):
    fig = px.histogram(data, x='odometer', title='Histograma del Odómetro')
    st.plotly_chart(fig)

# Scatterplot de precio vs. año del modelo
if st.checkbox('Mostrar gráfico de dispersión Precio vs. Año del Modelo'):
    fig = px.scatter(data, x='model_year', y='price', title='Precio vs. Año del Modelo')
    st.plotly_chart(fig)