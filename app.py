import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('D:\\descarga\\vehicles_us.csv')

# Crear un menú desplegable para seleccionar coches
selected_car = st.selectbox('Seleccionar coche', car_data['manufacturer'].unique())

# Filtrar los datos basándose en el coche seleccionado
filtered_data = car_data[car_data['manufacturer'] == selected_car]

# Crear un menú desplegable para seleccionar el modelo
selected_model = st.selectbox('Seleccionar modelo', filtered_data['model'].unique())

# Filtrar los datos basándose en el modelo seleccionado
filtered_data = filtered_data[filtered_data['model'] == selected_model]

# Crear un menú desplegable para seleccionar el año
selected_year = st.selectbox('Seleccionar año', filtered_data['year'].unique())

# Filtrar los datos basándose en el año seleccionado
filtered_data = filtered_data[filtered_data['year'] == selected_year]

# Crear una casilla de verificación para el histograma
build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # si la casilla de verificación está seleccionada
    # Escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un histograma
    fig = px.histogram(filtered_data, x="odometer")
    
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Crear una casilla de verificación para el gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter: # si la casilla de verificación está seleccionada
    # Escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un gráfico de dispersión
    fig = px.scatter(filtered_data, x="odometer", y="price")
    
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)