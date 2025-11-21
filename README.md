# mi-pipeline
Pipeline ETL automatizado para procesamiento de datos del clima actual

## 📋 Descripción

Weather ETL Pipeline es un pipeline end-to-end desarrollado con Apache Airflow, ejecutado localmente mediante Docker Compose, que automatiza la extracción, transformación y carga de datos del clima.
El flujo consulta una fuente de datos climáticos (simulada o API real), calcula métricas derivadas (como temperatura en Fahrenheit e índice de confort), y finalmente almacena los resultados en un archivo JSON para análisis posterior.

Este proyecto fue desarrollado como parte del taller "Mi Primer Pipeline con Airflow", integrando buenas prácticas de orquestación y diseño ETL.

## 🎯 Objetivos

- Extraer información meteorológica de una fuente externa.
- Transformar y enriquecer los datos con estadísticas relevantes.
- Generar un índice de confort basado en temperatura y humedad.
- Cargar el resultado procesado en un archivo JSON para persistencia.
- Ejecutar y monitorear el pipeline de manera completamente automática mediante Airflow.

## 🛠️ Stack Tecnológico

- **Apache Airflow 2.7+** – Orquestación del pipeline
- **Docker & Docker Compose** – Entorno reproducible
- **Python 3.9+** – Transformaciones y lógica ETL
- **JSON** – Almacenamiento del resultado
- **Airflow PythonOperator** – Ejecución de tareas

## 📁 Estructura del Proyecto

weather-pipeline/
├── dags/
│   └── pipeline_clima.py      # DAG principal ETL
├── docker-compose.yaml         # Orquestación Airflow con Docker
├── requirements.txt            # Dependencias adicionales (opcional)
└── README.md                   # Documentación

## 🌡️ ¿Qué problema resuelve este pipeline?

- Este pipeline permite responder preguntas como:
- ¿Cuál es la temperatura actual en mi ciudad?
- ¿Cómo se comporta la humedad junto con la temperatura?
- ¿Qué tan cómodo se percibe el clima en base a sus condiciones?
- ¿Cómo registrar automáticamente datos del clima para análisis diario/horario?
- Es útil para dashboards personales, análisis de tendencias o experimentos de datos.

## 🔍 Flujo del Pipeline (ETL)

**1. Extract**
- Obtiene datos climáticos de una API o fuente simulada (ciudad, temperatura, humedad, fecha).

**2. Transform**
- Cálculo de temperatura en Fahrenheit.
- Cálculo de un Índice de Confort según reglas simples.
- Enriquecimiento de los datos originales.

**3. Load**
- Almacena los datos transformados en un archivo JSON dentro del contenedor (por defecto /tmp).

## 🖥️ DAG en Airflow

El pipeline está compuesto por 3 tareas encadenadas:
```bash
extraer → calcular → guardar
```

## 🚀 Instalación y Ejecución

**1. Prerrequisitos**

- Docker Desktop instalado.
- Docker Compose habilitado.
- 4GB de RAM disponibles.

**2. Clonar el repositorio**
```bash
git clone https://github.com/santiago-izurieta-data/mi-pipeline.git
cd mi-pipeline
```

**3. (Opcional) Agregar librerías extra**
```bash
requests
pandas
```

**4. Inicializar Airflow**
```bash
docker compose up airflow-init
```

**5. Levantar los servicios**
```bash
docker compose up -d
```

**6. Acceder al UI de Airflow**
- URL: http://localhost:8080
- Usuario: airflow
- Password: airflow

## 💻 Uso
**Activar y ejecutar el DAG**
1. En la interfaz de Airflow, activa el DAG pipeline_clima.
2. Haz clic en ▶️ para ejecutar manualmente.
3. Observa el flujo desde la vista Graph.
4. Abre los logs para ver detalles de cada tarea.

## 📊 Resultados

- Generación automática de archivos JSON diarios/horarios con datos enriquecidos.
- Pipeline confiable y reproducible gracias a Airflow + Docker.
- Flujo ETL modular y extensible.
- Capacidad para conectarse a APIs reales sin modificar la arquitectura.

## 🔄 Pipeline Flow
```bash
API/Sources → EXTRACT → TRANSFORM → LOAD → Archivo JSON (/tmp)
```

## 📈 Próximas Mejoras

 - Integración con una API real como OpenWeatherMap.
 - Guardar datos en PostgreSQL o DuckDB.
 - Dashboard en Grafana o Streamlit.
 - Parametrización del DAG para múltiples ciudades.
 - Pruebas unitarias (pytest + Airflow DAG tests).

## 📝 Licencia

Este proyecto está bajo licencia MIT. Consulta el archivo LICENSE para más detalles.

## 👤 Autor

Santiago Izurieta

LinkedIn: https://ec.linkedin.com/in/santiago-izurieta-844324125

Portfolio: https://my-data-engineer-folio.lovable.app/

## 🙏 Agradecimientos

- Comunidad de Apache Airflow
- Proyecto del taller “Mi Primer Pipeline con Airflow”
- Documentación oficial de Docker y Airflow