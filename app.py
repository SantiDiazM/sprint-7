import pandas as pd
import plotly.express as px
import streamlit as st


car_data = pd.read_csv("vehicles_us.csv")

st.header("Análisis de anuncios de vehículos")

st.write("Selecciona los gráficos que deseas visualizar.")

build_histogram = st.checkbox("Mostrar histograma")

if build_histogram:
    st.write("Distribución del kilometraje")

    fig = px.histogram(
        car_data,
        x="odometer",
        title="Distribución del kilometraje"
    )

    st.plotly_chart(fig)


build_scatter = st.checkbox("Mostrar diagrama de dispersión")

if build_scatter:
    st.write("Relación entre el kilometraje y el precio")

    fig = px.scatter(
        car_data,
        x="odometer",
        y="price",
        title="Precio según el kilometraje"
    )

    st.plotly_chart(fig)