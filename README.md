
## ****NYC Taxis & Carbon Emission****
<p align= "center">
<img src= "https://i.postimg.cc/j5pWYDXX/Blue-Purple-Futuristic-Modern-3-D-Tech-Company-Business-Presentation-1.jpg", width= "70%">
</p>

# Objetivo General:
Evaluar la viabilidad de incorporar vehículos eléctricos en la flota de transporte de pasajeros de la empresa, con el fin de reducir las emisiones contaminantes y la contaminación sonora, basándose en el análisis de datos de taxis de Nueva York, así como en información relacionada con la calidad del aire y los niveles de ruido urbano.

### 1. Definición del Problema y Objetivos
 Analizar la relación entre el transporte de taxis y viajes compartidos en Nueva York con la calidad del aire y la contaminación sonora para evaluar la viabilidad de implementar vehículos eléctricos.

**Objetivos Específicos:**
-   **Recopilar y depurar datos** de diferentes fuentes, incluyendo taxis y viajes compartidos en Nueva York.
-   Cruzar estos datos con información de calidad del aire, contaminación sonora y datos climáticos.    
-   Realizar un análisis exploratorio de datos (EDA) para identificar patrones y relaciones significativas.    
-   Entrenar un modelo de machine learning para predecir o clasificar la contaminación basada en los datos de transporte.
-   Proveer recomendaciones basadas en los análisis y modelos desarrollados.

### 2. Recopilación de Datos

**Fuentes de Datos:**
-   NYC Taxi & Limousine Commission (TLC): Datos históricos de viajes en taxis y viajes compartidos.
-   Calidad del Aire: Datos provenientes de estaciones de monitoreo de calidad del aire, como los proporcionados por la EPA (Environmental Protection Agency) o NYC Open Data.
-   Contaminación Sonora: Datos de niveles de ruido urbano disponibles en NYC Open Data.    
-   Condiciones Climáticas: Datos históricos de clima, como temperatura y humedad, que pueden influir en el uso de taxis.

**Métodos de Extracción:**
-   APIs: Acceso a datos climáticos y de calidad del aire a través de APIs como la de OpenWeatherMap o AirVisual. 
-   Web Scraping: Recolección de datos de sitios web que no proporcionan APIs, como informes de contaminación sonora.    
-   Archivos CSV/Excel: Datos estáticos de viajes de taxi y contaminación sonora disponibles en formato descargable.

### 3. Depuración y Almacenamiento de los Datos

**Procesos de Limpieza:**
-   Manejo de valores nulos, duplicados y datos inconsistentes.    
-   Conversión de tipos de datos y formatos para la integración correcta entre datasets.    
-   Desanidación de columnas que contengan listas o diccionarios para facilitar su análisis.
    
**Almacenamiento:**
-   Creación de un Data Warehouse que centralice todos los datos. Puede estar alojado en local (e.g., PostgreSQL) o en la nube (e.g., AWS Redshift, Google BigQuery).

### 4. Análisis Exploratorio de Datos (EDA)

**Análisis a Realizar:**
-   Identificación de patrones de uso de taxis en función de variables temporales (día de la semana, hora, temporada).    
-   Análisis de correlación entre la actividad de los taxis y los niveles de contaminación sonora y calidad del aire.    
-   Visualizaciones que muestren la relación espacial entre la actividad de los taxis y la contaminación en diferentes zonas de la ciudad.
    

### 5. Modelado de Machine Learning

**Modelo a Desarrollar:**
-   Un modelo de clasificación supervisado, como Random Forest o Gradient Boosting, para predecir los niveles de contaminación en base a la actividad de los taxis.
<p align= "center">
<img src= "https://i.postimg.cc/Z5XQ6js5/machine-learn.jpg", width= "20%", height= "20%">
<br/>
</p>

**Proceso de Entrenamiento:**

-   División de los datos en conjuntos de entrenamiento y prueba.   
-   Evaluación del modelo utilizando métricas adecuadas (accuracy, precision, recall, etc.).
-   Ajuste de hiperparámetros para optimizar el rendimiento.

### 6. Implementación y Puesta en Producción

Despliegue del Modelo:

-   Desarrollar una APP con Streamlit para disponibilizar las predicciones del modelo.

-   Creación de un dashboard en Streamlit o Power BI que muestre los análisis y predicciones en tiempo real.

<p align= "center">
<img src= "https://i.postimg.cc/JhJ2xJSc/Amazon-Web-Services-AWS-Logo.png", width= "20%", height= "20%"> <img src= "https://i.postimg.cc/htpK1FW1/Quick-Sight-amazon.webp", width= "12%", height= "10%">
<br/>
</p>

### 7. Reporte y Recomendaciones

**Informe Final:**
-   Resumen de los hallazgos más importantes del análisis exploratorio y del modelo.    
-   Evaluación de la viabilidad de implementar vehículos eléctricos en la flota basada en los resultados obtenidos.    
-   Recomendaciones para la empresa en cuanto a la implementación de soluciones más amigables con el medio ambiente.
    
### 8. Plan de Acción Futuro

**Pasos Siguientes:**
-   Expansión del análisis a otras ciudades para obtener un marco de referencia más amplio.   
-   Integración de datos adicionales como el comportamiento de los usuarios frente a opciones de movilidad sostenible.    
-   Continuar el monitoreo y ajuste del modelo a medida que se obtengan nuevos datos.
   
Este plan abarca todas las etapas críticas para el desarrollo del proyecto, desde la recolección de datos hasta la implementación de soluciones de machine learning, con el objetivo de proporcionar a la empresa una base sólida para tomar decisiones estratégicas en su nueva unidad de negocio.

## primer sprint

Queremos ayudar a empresas de transporte de pasajeros a tomar decisiones fundamentadas sobre la implementación de vehículos eléctricos en su flota. Para ello, se analizan los datos de movimientos de taxis en Nueva York y su relación con la calidad del aire y la contaminación sonora, entre otros factores ambientales. A continuación, se detalla un plan de trabajo para desarrollar este proyecto

## Segundo sprint

En esta segunda etapa, se enfoco en el procesamiento y análisis de los datos recopilados usando el servicio de la nube AWS desarrollando un proceso automatizado de ETL (Extracción, Transformación y Carga) cumpliendo con el ciclo de vida de los datos desde la captura inicial hasta la generación de informes y visualizaciones para el uso en la aplicacion de machine learning y el dashboard.

## Tercer sprint

En esta ultima etapa se desarrollo un modelo de machine learning para implementarlo en la aplicacion de streamlit para la predicción de precios en los viajes de taxis en la ciudad de Nueva York, Se hizo enfasis en el diseño del dashboard contemplando los colores y los graficos a usar para tener un una interfaz amigable para el usuario donde se pueda explorar los datos evaluar los kpis  que facilite el análisis y llegar a tomar decisiones estrategicas.

## Tecnologías usadas en el proyecto

### Comunicación y trabajo en equipo

![My Skills](https://skillicons.dev/icons?i=discord&theme=dark&perline=15)
![My Skills](https://go-skill-icons.vercel.app/api/icons?i=slack,jira,googlemeet&titles=true)

### Desarrollo del proyecto

![My Skills](https://skillicons.dev/icons?i=python&theme=dark&perline=15)
![My Skills](https://go-skill-icons.vercel.app/api/icons?i=pandas,scikitlearn,numpy,git,streamlit,aws&titles=true)

### Link de la aplicación:

[![EasyTrip](https://go-skill-icons.vercel.app/api/icons?i=android&titles=true)](https://pftaxisny-p2yxafytih7czw8pe5xygj.streamlit.app/)

### Link del Dashboard:

[![EasyTrip](https://go-skill-icons.vercel.app/api/icons?i=aws&titles=true)](https://us-east-1.quicksight.aws.amazon.com/sn/dashboards/c2d87f9c-9348-4c42-b40e-c1fcea04fc71/sheets/c2d87f9c-9348-4c42-b40e-c1fcea04fc71_1800b16a-6f64-4519-bf7b-c4de47fef04c)


## Autores
| [<img src="https://avatars.githubusercontent.com/u/143465990?s=64&v=4" width=100><br><sub>Andres Acosta</sub>](https://github.com/EAndresAcosta) | [<img src="https://avatars.githubusercontent.com/u/88012655?v=4" width=100><br><sub>GonzaloHC</sub>](https://github.com/GonzaloHC) | [<img src="https://avatars.githubusercontent.com/u/56074646?v=4" width=100><br><sub>MariamV27</sub>](https://github.com/MariamV27) | [<img src="https://avatars.githubusercontent.com/u/125500094?v=4" width=100><br><sub>Danilo Carranza</sub>](https://github.com/CarranzaDanilo) |
|:---:|:---:|:---:|:---:|