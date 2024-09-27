
## ****NYC Taxis & Carbon Emission**** 

<p align="center">
<img src="https://i.postimg.cc/TYqKBYWV/Screenshot-2024-09-24-at-22-13-51.png", height="400px", width="420px">
<br/>
</p>

**Getting Started**
Queremos ayudar a empresas de transporte de pasajeros a tomar decisiones fundamentadas sobre la implementación de vehículos eléctricos en su flota. Para ello, se analizan los datos de movimientos de taxis en Nueva York y su relación con la calidad del aire y la contaminación sonora, entre otros factores ambientales. A continuación, se detalla un plan de trabajo para desarrollar este proyecto:

**KPI's** Evaluar la viabilidad de incorporar vehículos eléctricos en la flota de transporte de pasajeros de la empresa, con el fin de reducir las emisiones contaminantes y la contaminación sonora, basándose en el análisis de datos de taxis de Nueva York, así como en información relacionada con la calidad del aire y los niveles de ruido urbano.

<p align="center">
<img src="https://i.postimg.cc/90yDmcgj/Screenshot-2024-09-25-at-14-26-16.png", height="450px", width="600px">
<br/>
</p>

## Architecture
### Arquitectura AWS - Pipeline de Datos
La arquitectura ilustra un flujo de datos en la nube de AWS desde el almacenamiento local hasta la visualización, utilizando varios servicios de AWS.

## Flow Description:

### 1. Almacenamiento Local
El sistema parte desde un **almacenamiento local** (Filestore), que contiene un archivo de datos en formato **Parquet** llamado `Trip_taxis.parquet`.

### 2. Carga a AWS
Los datos son cargados desde el almacenamiento local a un **bucket de Amazon S3** (Source Bucket) en la nube de AWS.

### 3. Descubrimiento de Datos
Una vez en el bucket de S3, el servicio **AWS Glue Crawler** explora los datos y genera el esquema de los mismos. Este esquema se registra en el **Glue Data Catalog**, el cual actúa como un catálogo de metadatos para los conjuntos de datos disponibles.

### 4. Transformación de Datos
Con los metadatos registrados en el **Glue Data Catalog**, se pueden realizar consultas y transformaciones a través de:
- **Amazon Athena**: Servicio que permite ejecutar consultas SQL directamente sobre los datos en S3, utilizando los metadatos del Glue Data Catalog.
- **AWS Glue**: Servicio que realiza la extracción y transformación (ETL) de los datos basándose en el catálogo.

### 5. Almacenamiento en Data Warehouse
Una vez transformados, los datos se cargan en **Amazon Redshift**, un servicio de almacenamiento y análisis de datos a gran escala (Data Warehouse).

### 6. Visualización de los Datos
Los datos almacenados en **Amazon Redshift** pueden ser visualizados mediante **Amazon QuickSight**, una herramienta de inteligencia empresarial (BI) que genera informes y dashboards interactivos.

## Servicios Utilizados:

- **Amazon S3**: Almacenamiento de objetos en la nube.
- **AWS Glue Crawler**: Descubre los datos y genera el esquema automáticamente.
- **Glue Data Catalog**: Almacena los metadatos de los datos procesados.
- **AWS Glue**: Realiza trabajos de extracción, transformación y carga (ETL).
- **Amazon Athena**: Consulta interactiva de datos en S3 usando SQL.
- **Amazon Redshift**: Almacenamiento de datos escalable y de alto rendimiento.
- **Amazon QuickSight**: Herramienta de visualización de datos e inteligencia empresarial.

![enter image description here](https://i.postimg.cc/HWMc4tYP/Whats-App-Image-2024-09-20-at-15-49-12.jpg)

Este flujo de trabajo permite el manejo de grandes volúmenes de datos con transformación, almacenamiento y análisis eficientes mediante los servicios de AWS.

Enlace de la aplicación:

[EASYTRIP](https://pftaxisny-p2yxafytih7czw8pe5xygj.streamlit.app/)

Enlace del Dashboard:

[Dashboard](https://us-east-1.quicksight.aws.amazon.com/sn/dashboards/c2d87f9c-9348-4c42-b40e-c1fcea04fc71/sheets/c2d87f9c-9348-4c42-b40e-c1fcea04fc71_1800b16a-6f64-4519-bf7b-c4de47fef04c)

