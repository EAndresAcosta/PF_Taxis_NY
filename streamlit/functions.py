import pandas as pd
from opencage.geocoder import OpenCageGeocode
import requests
from requests.exceptions import ConnectionError, Timeout, RequestException
import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster, HeatMap
import streamlit as st
from dotenv import load_dotenv
import os
import time

# Cargar las variables del archivo .env
load_dotenv()

# API key de OpenCage
api_key = os.getenv("OPENCAGE_API_KEY")
geocoder = OpenCageGeocode(api_key)

# Cargar los datos de calidad del aire al inicio
data_calidad_aire = pd.read_csv('streamlit/data/CD_air.csv')  # Asegúrate de que esta ruta sea correcta

# Calcular promedios de contaminantes por zona, excluyendo valores extremos
promedios_calidad_aire = data_calidad_aire.groupby(['cd_name', 'polluting_agent'])['data_value'].apply(
    lambda x: x.clip(lower=x.quantile(0.05), upper=x.quantile(0.95)).mean()
).reset_index()

# Crear un diccionario para almacenar promedios por zona
calidad_aire_por_zona = {}
for _, row in promedios_calidad_aire.iterrows():
    zona = row['cd_name']
    contaminante = row['polluting_agent']
    promedio = row['data_value']
    
    if zona not in calidad_aire_por_zona:
        calidad_aire_por_zona[zona] = {}
    calidad_aire_por_zona[zona][contaminante] = promedio

# Definir coordenadas para cada zona
coordenadas_zonas = {
    'Sunset Park (CD7)': [40.6456, -74.0026],
    'Coney Island (CD13)': [40.5734, -73.9867],
    'Midtown (CD5)': [40.7549, -73.9845],
    'Upper West Side (CD7)': [40.7851, -73.9735],
    'Sheepshead Bay (CD15)': [40.6060, -73.9525],
    'Ridgewood and Maspeth (CD5)': [40.6949, -73.9063],
    'Elmhurst and Corona (CD4)': [40.7402, -73.8659],
    'Bushwick (CD4)': [40.6880, -73.9169],
    'Williamsbridge and Baychester (CD12)': [40.8742, -73.8517],
    'Parkchester and Soundview (CD9)': [40.8260, -73.8550],
    'East New York and Starrett City (CD5)': [40.6662, -73.8840],
    'South Beach and Willowbrook (CD2)': [40.5757, -74.0734],
    'Queens Village (CD13)': [40.7401, -73.7492],
    'Bedford Stuyvesant (CD3)': [40.6850, -73.9476],
    'Bensonhurst (CD11)': [40.6055, -73.9947],
    'St. George and Stapleton (CD1)': [40.6404, -74.0794],
    'Greenpoint and Williamsburg (CD1)': [40.7225, -73.9462],
    'Hunts Point and Longwood (CD2)': [40.8204, -73.8954],
    'Long Island City and Astoria (CD1)': [40.7463, -73.9523],
    'Fordham and University Heights (CD5)': [40.8643, -73.8965],
    'Jackson Heights (CD3)': [40.7497, -73.8862],
    'Jamaica and Hollis (CD12)': [40.7103, -73.7822],
    'Crown Heights and Prospect Heights (CD8)': [40.6694, -73.9442],
    'Riverdale and Fieldston (CD8)': [40.8940, -73.9148],
    'Fort Greene and Brooklyn Heights (CD2)': [40.6954, -73.9920],
    'Belmont and East Tremont (CD6)': [40.8430, -73.8650],
    'Bayside and Little Neck (CD11)': [40.7715, -73.7558],
    'Upper East Side (CD8)': [40.7755, -73.9499],
    'Lower East Side and Chinatown (CD3)': [40.7189, -73.9831],
    'Highbridge and Concourse (CD4)': [40.8481, -73.9245],
    'Mott Haven and Melrose (CD1)': [40.8126, -73.9118],
    'East Flatbush (CD17)': [40.6460, -73.9412],
    'Flatbush and Midwood (CD14)': [40.6237, -73.9507],
    'East Harlem (CD11)': [40.7972, -73.9430],
    'Morningside Heights and Hamilton Heights (CD9)': [40.8182, -73.9641],
    'Rockaway and Broad Channel (CD14)': [40.5907, -73.8145],
    'Kew Gardens and Woodhaven (CD9)': [40.7062, -73.8420],
    'Brownsville (CD16)': [40.6508, -73.9114],
    'Morrisania and Crotona (CD3)': [40.8437, -73.9033],
    'Stuyvesant Town and Turtle Bay (CD6)': [40.7312, -73.9754],
    'Washington Heights and Inwood (CD12)': [40.8537, -73.9342],
    'Bay Ridge and Dyker Heights (CD10)': [40.6230, -74.0217],
    'Clinton and Chelsea (CD4)': [40.7468, -74.0049],
    'Borough Park (CD12)': [40.6221, -73.9881],
    'Throgs Neck and Co-op City (CD10)': [40.8498, -73.8271],
    'Rego Park and Forest Hills (CD6)': [40.7180, -73.8511],
    'Flushing and Whitestone (CD7)': [40.7758, -73.8354],
    'Hillcrest and Fresh Meadows (CD8)': [40.7215, -73.8183],
    'South Ozone Park and Howard Beach (CD10)': [40.6704, -73.8265],
    'Financial District (CD1)': [40.7074, -74.0113],
    'Greenwich Village and Soho (CD2)': [40.7305, -74.0020],
    'South Crown Heights and Lefferts Gardens (CD9)': [40.6554, -73.9420],
    'Tottenville and Great Kills (CD3)': [40.5006, -74.2430],
    'Kingsbridge Heights and Bedford (CD7)': [40.8695, -73.8984],
    'Park Slope and Carroll Gardens (CD6)': [40.6756, -73.9963],
    'Morris Park and Bronxdale (CD11)': [40.8501, -73.8576],
    'Central Harlem (CD10)': [40.8116, -73.9465],
    'Flatlands and Canarsie (CD18)': [40.6340, -73.9051],
    'Woodside and Sunnyside (CD2)': [40.7400, -73.9114]
}

lugares_recomendados = [
'Allerton/Pelham Gardens', 'Alphabet City', 'Arrochar/Fort Wadsworth', 'Astoria Park',
'Auburndale', 'Bath Beach', 'Battery Park', 'Battery Park City',
'Bay Ridge', 'Bay Terrace/Fort Totten', 'Bayside', 'Bedford', 'Bedford Park',
'Bellerose', 'Belmont', 'Bensonhurst East', 'Bensonhurst West', 'Bloomfield/Emerson Hill',
'Bloomingdale', 'Boerum Hill', 'Borough Park', 'Breezy Point/Fort Tilden/Riis Beach', 'Briarwood/Jamaica Hills',
'Brighton Beach', 'Broad Channel', 'Bronx Park', 'Bronxdale', 'Brooklyn Heights',
'Brooklyn Navy Yard', 'Brownsville', 'Bushwick North', 'Bushwick South', 'Cambria Heights',
'Canarsie', 'Carroll Gardens', 'Central Harlem', 'Central Harlem North', 'Central Park',
'Charleston/Tottenville', 'Chinatown', 'City Island', 'Claremont/Bathgate', 'Clinton East',
'Clinton Hill', 'Clinton West', 'Co-Op City', 'Cobble Hill', 'College Point',
'Columbia Street', 'Coney Island', 'Corona', 'Country Club', 'Crotona Park',
'Crotona Park East', 'Crown Heights North', 'Crown Heights South', 'Cypress Hills', 'DUMBO/Vinegar Hill',
'Douglaston', 'Downtown Brooklyn/MetroTech', 'Dyker Heights', 'East Chelsea', 'East Concourse/Concourse Village',
'East Elmhurst', 'East Flatbush/Farragut', 'East Flatbush/Remsen Village', 'East Flushing', 'East Harlem North',
'East Harlem South', 'East New York', 'East New York/Pennsylvania Avenue', 'East Tremont', 'East Village',
'East Williamsburg', 'Eastchester', 'Elmhurst', 'Elmhurst/Maspeth', 'Erasmus',
'Far Rockaway', 'Financial District North', 'Financial District South', 'Flatbush/Ditmas Park', 'Flatiron',
'Flatlands', 'Flushing', 'Flushing Meadows-Corona Park', 'Fordham South', 'Forest Hills',
'Forest Park/Highland Park', 'Fort Greene', 'Fresh Meadows', 'Garment District', 'Glen Oaks',
'Glendale', "Governor's Island/Ellis Island/Liberty Island", 'Gowanus', 'Gramercy', 'Gravesend',
'Green-Wood Cemetery', 'Greenpoint', 'Greenwich Village North', 'Greenwich Village South', 'Hamilton Heights',
'Hammels/Arverne', 'Heartland Village/Todt Hill', 'Highbridge', 'Highbridge Park', 'Hillcrest/Pomonok',
'Hollis', 'Homecrest', 'Howard Beach', 'Hudson Sq', 'Hunts Point',
'Inwood', 'Inwood Hill Park', 'JFK Airport', 'Jackson Heights', 'Jamaica',
'Jamaica Bay', 'Jamaica Estates', 'Kensington', 'Kew Gardens', 'Kew Gardens Hills',
'Kingsbridge Heights', 'Kips Bay', 'LaGuardia Airport', 'Laurelton', 'Lenox Hill East',
'Lenox Hill West', 'Lincoln Square East', 'Lincoln Square West', 'Little Italy/NoLiTa', 'Long Island City/Hunters Point',
'Long Island City/Queens Plaza', 'Longwood', 'Lower East Side', 'Madison', 'Manhattan Beach',
'Manhattan Valley', 'Manhattanville', 'Marble Hill', 'Marine Park/Floyd Bennett Field', 'Marine Park/Mill Basin',
'Mariners Harbor', 'Maspeth', 'Meatpacking/West Village West', 'Melrose South', 'Middle Village',
'Midtown Center', 'Midtown East', 'Midtown North', 'Midtown South', 'Midwood',
'Morningside Heights', 'Morrisania/Melrose', 'Mott Haven/Port Morris', 'Mount Hope', 'Murray Hill',
'Murray Hill-Queens', 'New Dorp/Midland Beach', 'Newark Airport', 'North Corona', 'Norwood',
'Oakland Gardens', 'Oakwood', 'Ocean Hill', 'Ocean Parkway South', 'Old Astoria',
'Ozone Park', 'Park Slope', 'Parkchester', 'Pelham Bay', 'Pelham Bay Park',
'Pelham Parkway', 'Penn Station/Madison Sq West', 'Prospect Heights', 'Prospect Park', 'Prospect-Lefferts Gardens',
'Queens Village', 'Queensboro Hill', 'Queensbridge/Ravenswood', 'Randalls Island', 'Red Hook',
'Rego Park', 'Richmond Hill', 'Ridgewood', 'Rikers Island', 'Riverdale/North Riverdale/Fieldston',
'Rockaway Park', 'Roosevelt Island', 'Rosedale', 'Saint Albans', 'Saint George/New Brighton',
'Saint Michaels Cemetery/Woodside', 'Schuylerville/Edgewater Park', 'Seaport', 'Sheepshead Bay', 'SoHo',
'Soundview/Bruckner', 'Soundview/Castle Hill', 'South Jamaica', 'South Ozone Park', 'South Williamsburg',
'Springfield Gardens North', 'Springfield Gardens South', 'Spuyten Duyvil/Kingsbridge', 'Stapleton', 'Starrett City',
'Steinway', 'Stuy Town/Peter Cooper Village', 'Stuyvesant Heights', 'Sunnyside', 'Sunset Park East',
'Sunset Park West', 'Sutton Place/Turtle Bay North', 'Times Sq/Theatre District', 'TriBeCa/Civic Center', 'Two Bridges/Seward Park', 'UN/Turtle Bay South', 'Union Sq', 'University Heights/Morris Heights', 'Upper East Side North',
'Upper East Side South', 'Upper West Side North', 'Upper West Side South', 'Van Cortlandt Park', 'Van Cortlandt Village',
'Van Nest/Morris Park', 'Washington Heights North', 'Washington Heights South', 'West Brighton', 'West Chelsea/Hudson Yards',
'West Concourse', 'West Farms/Bronx River', 'West Village', 'Westchester Village/Unionport', 'Westerleigh',
'Whitestone', 'Willets Point', 'Williamsbridge/Olinville', 'Williamsburg (North Side)', 'Williamsburg (South Side)',
'Windsor Terrace', 'Woodhaven', 'Woodlawn/Wakefield', 'Woodside', 'World Trade Center',
'Yorkville East', 'Yorkville West'
]

def lugar_input(label):
    """
    Crea un input que permite al usuario seleccionar un lugar de una lista o escribir uno personalizado.
    
    Parameters:
    - label: El texto que se mostrará en el input.
    
    Returns:
    - str: El lugar seleccionado o el lugar personalizado escrito por el usuario.
    """
    # Selectbox para lugares recomendados
    selected_lugar = st.selectbox(label, options=lugares_recomendados, key=f"select_{label}")

    # Si se selecciona "Otro", mostrar el text input
    if selected_lugar == "Otro":
        return st.text_input("✍️ O escribe tu lugar favorito:", placeholder="Escribe aquí...", key=f"text_{label}")

    return selected_lugar

def obtener_coordenadas(query: str): 

    results = geocoder.geocode(query)

    if results:
        # Devuelve la primera coincidencia
        latitude = results[0]['geometry']['lat']
        longitude = results[0]['geometry']['lng']
        return latitude, longitude

    return None, None

def obtener_ruta(lat_inicio, lon_inicio, lat_destino, lon_destino, reintentos=3, espera=2):

    url = f"http://router.project-osrm.org/route/v1/driving/{lon_inicio},{lat_inicio};{lon_destino},{lat_destino}?overview=false"

    for intento in range(reintentos):
        try:
            response = requests.get(url, timeout=10)  # Tiempo de espera de 10 segundos
            response.raise_for_status()  # Lanza excepción si hay un error HTTP
            data = response.json()
            
            if data['code'] == 'Ok':
                ruta = data['routes'][0]
                tiempo = int(round(int(ruta['duration']) / 60, 0))
                distancia = round(int(ruta['distance']) * 0.000621371, 2)
                return tiempo, distancia
            else:
                print(f"Error en la respuesta de OSRM: {data['code']}")
                return None, None
        
        except (ConnectionError, Timeout) as e:
            print(f"Error de conexión o tiempo de espera agotado: {e}. Reintentando ({intento + 1}/{reintentos})...")
            time.sleep(espera)  # Espera antes de reintentar

        except RequestException as e:
            print(f"Error al procesar la solicitud: {e}")
            break

    # Si llega aquí, significa que fallaron todos los intentos
    print("No se pudo obtener la ruta después de varios intentos.")
    return None, None
    
def mostrar_mapa(lat_origen, lon_origen, lat_destino, lon_destino):
    """Mostrar un mapa con la ruta y marcadores de calidad del aire."""

    url = f'http://router.project-osrm.org/route/v1/driving/{lon_destino},{lat_destino};{lon_origen},{lat_origen}?overview=full&geometries=geojson'
    
    max_retries = 5
    retries = 0

    # Hacer la solicitud a la API de OSRM
    while retries < max_retries:
        response = requests.get(url)

        # Verifica si la solicitud fue exitosa
        if response.status_code == 200:
            try:
                data = response.json()
                break
            except ValueError:
                retries += 1
                st.warning("Intentando de nuevo... fallo en decodificar JSON.")
                time.sleep(2)
        else:
            retries += 1
            st.warning(f"Intentando de nuevo... Código de estado: {response.status_code}")
            time.sleep(2)
        if retries == max_retries:
            st.error("No se pudo obtener la información después de varios intentos.")
            return

    # Extraer los puntos de la ruta
    route = data['routes'][0]['geometry']
    route_points = [(coord[1], coord[0]) for coord in route['coordinates']]

    # Crear un mapa centrado en las coordenadas de origen
    m = folium.Map(location=[lat_origen, lon_origen], zoom_start=10)

    # Agregar la ruta al mapa
    folium.PolyLine(route_points, color="blue").add_to(m)

    # Agregar un marcador verde en el origen
    folium.Marker(
        location=[lat_origen, lon_origen],
        popup="Origen",
        icon=folium.Icon(color="green")
    ).add_to(m)

    # Agregar un marcador rojo en el destino
    folium.Marker(
        location=[lat_destino, lon_destino],
        popup="Destino",
        icon=folium.Icon(color="red")
    ).add_to(m)

    # Crear el clúster de marcadores
    marker_cluster = MarkerCluster().add_to(m)

    # Crear una lista para el mapa de calor
    heat_data = []

    # Agregar datos al clúster y al mapa de calor
    for zone_name, contaminantes in calidad_aire_por_zona.items():
        if zone_name in coordenadas_zonas:
            lat, lon = coordenadas_zonas[zone_name]
            valor_no2 = contaminantes['Nitrogen dioxide (NO2)']
            heat_data.append([lat, lon, valor_no2])

            # Agregar un marcador al clúster
            folium.Marker(
                location=[lat, lon],
                popup=(
                    f"{zone_name}: "
                    f"Nitrogen dioxide(NO2) = {valor_no2:.2f}, "
                    f"Ozono O3(ppb) = {contaminantes['O3 (ppb)']:.2f}, "
                    f"Fine particles(PM 2.5) = {contaminantes['Fine particles (PM 2.5)']:.2f}"
                ),
                icon=folium.Icon(color='blue' if valor_no2 < 20 else 'orange' if valor_no2 < 40 else 'red')
            ).add_to(marker_cluster)

    # Agregar mapa de calor
    if heat_data:  # Asegúrate de que hay datos para mostrar
        HeatMap(heat_data, gradient={0: 'blue', 0.5: 'lime', 1: 'red'}, radius=25).add_to(m)

    # Mostrar el mapa en Streamlit
    folium_static(m)

# Ejecución principal
if __name__ == "__main__":
    # Obtener coordenadas de origen y destino
    lat_origen, lon_origen = obtener_coordenadas("Origen, Nueva York")  # Cambia "Origen" por la ubicación real
    lat_destino, lon_destino = obtener_coordenadas("Destino, Nueva York")  # Cambia "Destino" por la ubicación real

    # Obtener la ruta
    tiempo, distancia = obtener_ruta(lat_origen, lon_origen, lat_destino, lon_destino)

    # Mostrar el mapa con la ruta y la calidad del aire
    mostrar_mapa(lat_origen, lon_origen, lat_destino, lon_destino) 