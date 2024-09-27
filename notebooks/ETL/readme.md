# Proceso ETL en AWS

Este documento describe el proceso de ETL (Extract, Transform, Load) desarrollado en el ecosistema de AWS, utilizando los servicios S3, Glue, Glue Workflow, Crawler, Data Catalog, y Redshift. A continuación, se detallan los pasos realizados en cada servicio.

## Tabla de Contenidos
1. [Introducción](#introducción)
2. [Arquitectura](#arquitectura)
3. [Servicios Utilizados](#servicios-utilizados)
   - [S3](#s3)
   - [Glue](#glue)
   - [Glue Workflow](#glue-workflow)
   - [Crawler](#crawler)
   - [Data Catalog](#data-catalog)
   - [Redshift](#redshift)
4. [Flujo del Proceso ETL](#flujo-del-proceso-etl)
   - [Extracción](#extracción)
   - [Transformación](#transformación)
   - [Automatización con Glue Workflow](#automatización-con-glue-workflow)
   - [Carga](#carga)
5. [Conclusión](#conclusión)
6. [Capturas de Pantalla](#capturas-de-pantalla)

## Introducción
Este proyecto consiste en la implementación de un proceso ETL utilizando servicios de AWS para gestionar y analizar grandes volúmenes de datos. El objetivo principal es cargar datasets almacenados en S3, transformarlos mediante Glue y almacenar los resultados en un Data Warehouse (Redshift) para su análisis y consulta.

## Arquitectura
La arquitectura del proceso ETL consta de los siguientes componentes:

1. **Amazon S3**: Almacenamiento de datos fuente.
2. **AWS Glue**: Orquestación y transformación de datos.
3. **Glue Workflow**: Automatización del proceso ETL.
4. **Glue Crawler**: Descubrimiento de datos y creación de esquemas.
5. **Glue Data Catalog**: Gestión de metadatos y esquemas de datos.
6. **Amazon Redshift**: Almacenamiento de datos transformados para análisis.  

![alt text](https://i.postimg.cc/HLhCJv6L/Arquitectura.jpg)

## Servicios Utilizados

### S3
- **Descripción**: S3 se utiliza como repositorio de los datasets originales y transformados.
- **Funcionalidad**: Los archivos fuente son subidos a un bucket de S3, el cual es configurado para ser accesible desde Glue.


### Glue
- **Descripción**: Glue sirve como la herramienta principal para el proceso de ETL.
- **Funcionalidad**: 
  - Se crean trabajos de Glue (Jobs) para ejecutar scripts de transformación.


### Glue Workflow
- **Descripción**: Glue Workflow se utiliza para automatizar y coordinar el proceso ETL completo.
- **Funcionalidad**:
  - Se crean workflows que integran varios Jobs de Glue, permitiendo la automatización de todo el proceso.
  - El workflow gestiona la secuencia de ejecución, incluyendo la extracción, transformación y carga de datos.
  - Se programan eventos y dependencias para iniciar los Jobs automáticamente, reduciendo la intervención manual.

### Crawler
- **Descripción**: Crawler se utiliza para escanear los datasets en S3 y crear tablas en el Data Catalog.
- **Funcionalidad**:
  - Los crawlers se configuran para ejecutar de forma periódica y actualizar el Data Catalog con nuevos esquemas y datos.

### Data Catalog
- **Descripción**: Actúa como un repositorio centralizado de metadatos.
- **Funcionalidad**: El Data Catalog almacena los esquemas de las tablas generadas por los crawlers, lo que permite que Glue y Redshift accedan a los datos de manera organizada.

### Redshift
- **Descripción**: Redshift se utiliza como el Data Warehouse para almacenar los datos transformados.
- **Funcionalidad**:
  - Se crean tablas en Redshift para almacenar los resultados de las transformaciones.
  - Glue carga los datos transformados en las tablas de Redshift para su análisis y consulta.



## Flujo del Proceso ETL

### Extracción
1. **Carga de datos en S3**: Los archivos fuente se almacenan en un bucket de S3. 

### Transformación
1. **Configuración de Glue Crawler**: Se configura un crawler para identificar el esquema de los archivos en S3 y registrarlos en el Data Catalog.
2. **Desarrollo de Jobs en Glue**: Se crean scripts para la limpieza, transformación y enriquecimiento de los datos según las necesidades del negocio.

![alt text](https://i.postimg.cc/J0wVxDVV/job.png)

### Automatización con Glue Workflow
1. **Creación del Workflow**: Se diseña un Glue Workflow para integrar los distintos Jobs y etapas del proceso ETL.
2. **Programación de Tareas**: Se configuran las tareas y dependencias dentro del Workflow para asegurar que los Jobs se ejecuten en el orden correcto.
3. **Monitoreo y Alerta**: El Workflow incluye monitoreo y alertas para detectar fallos y asegurar la integridad del proceso.

![alt text](https://i.postimg.cc/BbxWVS48/workflow.png)

### Carga
1. **Carga de Datos a Redshift**: Los datos transformados se cargan en Amazon Redshift para su análisis.
2. **Validación y Verificación**: Se verifican los datos en Redshift para asegurar que cumplan con los requisitos del proyecto.

![alt text](https://i.postimg.cc/hjQRV8Y1/db.png)

## Conclusión
El uso de estos servicios permite un proceso ETL automatizado y escalable, que facilita la gestión y análisis de datos dentro del ecosistema de AWS. La implementación de Glue Workflow garantiza una automatización completa, reduciendo el esfuerzo manual y mejorando la eficiencia del proceso.

