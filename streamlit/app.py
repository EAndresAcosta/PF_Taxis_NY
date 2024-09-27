import streamlit as st
from joblib import load
import numpy as np
from functions import *


# Configurar la página
st.set_page_config(
    page_title="EasyTrip App",
    page_icon="🚖🛣️🗽🤗",
    layout="wide",  # Cambiar a ancho completo para la visualización óptima  
)
# Descargar el modelo desde la URL
# url = '../models/modelo_ridge.joblib?raw=True'
# response = requests.get(url)

modelo_path = './models/modelo_ridge.joblib'
modelo = load(modelo_path)

# Guardar el archivo en una ubicación temporal
# with open('modelo_ridge.joblib', 'wb') as f:
#     f.write(response.content)

# CSS para la imagen de fondo y estilos de texto
page_bg_img = '''
<style>
@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@200..700&display=swap');

[data-testid="stAppViewContainer"] {
    background-image: url("https://i.postimg.cc/mDFtdJT9/primer-plano-letrero-taxi-colocado.jpg");
    background-size: cover;
    background-repeat: no-repeat; /* Evitar repetición */
    background-attachment: fixed;  /* Fijar la imagen de fondo */
    background-position: center;
    color: white;
    font-family: 'Poppins', sans-serif;
}

.centered {
    text-align: center;
}

/* Título principal */
h1 {
    color: white;
    font-size: 56px;
    font-family: 'Oswald', sans-serif;
    font-weight: 700;
    text-align: center;
    text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
}

label, .stTextInput > div > div {
    color: white;
    font-family: 'Poppins', sans-serif;
}

.stTextInput > div > div > input {
    color: white;
    background-color: rgba(255, 255, 255, 0.1);
    font-family: 'Poppins', sans-serif;
}

.stButton > button {
    color: white;
    background-color: #00A693;
    font-family: 'Poppins', sans-serif;
    padding: 10px 20px;
    border-radius: 10px;
    border: none;
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
    transition: 0.3s ease;
}

.stButton > button:hover {
    background-color: #3B00DB;
}

/* Estilo para el mapa */
iframe {
    width: 100% !important;  /* El mapa ocupará el 100% del ancho */
    height: 500px !important;  /* Fijamos una altura mayor */
}

/* Hacer que el mapa y contenido sean responsivos */
[data-testid="stDataframeContainer"] {
    width: 100%;  /* Asegurar que el mapa se vea completo */
}

/* Ajustes para pantallas pequeñas */
@media (max-width: 768px) {
    h1 {
        font-size: 36px;  /* Ajustar tamaño del título para móviles */
    }

    .stTextInput > div > div {
        font-size: 14px;  /* Reducir tamaño de texto en móviles */
    }

    .stButton > button {
        padding: 8px 16px;  /* Hacer los botones más pequeños */
        font-size: 14px;
    }
}

/* Para pantallas más grandes, aseguramos que todo esté centrado */
[data-testid="stDataframeContainer"] {
    margin: 0 auto;  /* Centrar el mapa en pantallas grandes */
}

</style>
'''

# Cargar la imagen de fondo y estilos
st.markdown(page_bg_img, unsafe_allow_html=True)

# Parte del estilo
st.title("🚖 Bienvenido a EasyTrip la Experiencia Futurista de Viaje 🚀")
st.markdown("**Descubre el costo de tu viaje con un toque futurista. Ingrese las direcciones y déjanos hacer el resto.**", unsafe_allow_html=True)

# Definimos las ciudades en donde se opera 
ciudades = ['New York', 'Próximamente']

# Crear una barra de entrada para la dirección de origen
ciudad = st.selectbox(label="Selecciona una ciudad:", options=ciudades)
if ciudad == '🕑 Próximamente':
    st.write("⏳ **¡Pronto estaremos en más lugares emocionantes! Mantente atento.** 😎")
else:
    # Barra de entrada para dirección de origen
    direccion_origen = lugar_input("🗽Ingresa la dirección de origen:")
    
    # Barra de entrada para dirección de destino
    direccion_destino = lugar_input("🗺️ Ingresa la dirección de destino:")


# Añadir un botón para calcular la ruta
if st.button("💡 ¡Calcular Mi Viaje!"):
    # Inicializar variables
    tiempo = None
    distancia = None

    if direccion_origen == "" or direccion_destino == "":
        st.write("🚨 **Ups! Asegúrate de ingresar ambas direcciones.**")
    else:
        # Obtener coordenadas
        lat_origen, lon_origen = obtener_coordenadas(f"{direccion_origen}, {ciudad}")  # Asegurarse de incluir la ciudad en la búsqueda
        lat_destino, lon_destino = obtener_coordenadas(f"{direccion_destino}, {ciudad}")  # Asegurarse de incluir la ciudad en la búsqueda

        # Obtener tiempo y distancia
        tiempo, distancia = obtener_ruta(lat_origen, lon_origen, lat_destino, lon_destino)
        
        # Verificar que tiempo y distancia no sean NaN
        if np.isnan(tiempo) or np.isnan(distancia):
            st.write("😕 **No pudimos calcular la ruta. Por favor, revisa las direcciones.**")
        else:
            # Preparar los datos para el modelo
            new_data = np.array([[distancia, tiempo]])
            
            # Predecir la tarifa
            tarifa = modelo.predict(new_data)[0]
            
            # Mostrar resultados
            st.markdown("<h2 style='text-align: center; color: white;'>Datos del viaje y precio:</h2>", unsafe_allow_html=True)
            st.write(f"🗺️ **El mapa proporciona datos sobre la calidad del aire en distintas zonas de la ciudad: marcador color 🟦: calidad del aire buena, marcador color 🟨: calidad del aire moderada, marcador color 🟥: calidad del aire mala.**")
            st.write(f"⏱️ **Tiempo estimado:** {tiempo} minutos")
            st.write(f"🛣️ **Distancia:** {distancia} millas")
            st.write(f"💰 **Tarifa estimada:** ${round(tarifa, 1)}")

            mostrar_mapa(lat_origen, lon_origen, lat_destino, lon_destino)
            # Mostrar el mapa de calidad del aire