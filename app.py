import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Análisis de Datos de Vehículos')

data = pd.read_csv('notebooks/vehicles_us.csv')

st.header('Datos de Vehículos')
st.write(data.head())

if st.checkbox('Mostrar histograma del odómetro'):
    fig = px.histogram(data, x='odometer', title='Histograma del Odómetro')
    st.plotly_chart(fig)

if st.checkbox('Mostrar gráfico de dispersión Precio vs. Año'):
    fig = px.scatter(data, x='year', y='price', title='Precio vs. Año')
    st.plotly_chart(fig)