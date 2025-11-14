from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import json

def extraer_clima():
    """Simula extraer datos del clima"""
    # En un caso real, aquí llamarías a una API como OpenWeatherMap
    datos = {
        "ciudad": "Lima",
        "temperatura": 22,
        "humedad": 75,
        "fecha": str(datetime.now())
    }
    print(f"Datos extraídos: {datos}")
    return datos

def calcular_estadisticas(**context):
    """Calcula estadísticas básicas"""
    datos = context['ti'].xcom_pull(task_ids='extraer')
    
    # Calcular índice de confort (ejemplo simple)
    temp = datos['temperatura']
    humedad = datos['humedad']
    
    if temp > 25 and humedad > 70:
        confort = "Caluroso y húmedo"
    elif temp < 15:
        confort = "Frío"
    else:
        confort = "Agradable"
    
    resultado = {
        **datos,
        "indice_confort": confort,
        "temperatura_fahrenheit": temp * 1.8 + 32
    }
    
    print(f"Estadísticas calculadas: {resultado}")
    return resultado

def guardar_resultados(**context):
    """Guarda los resultados en un archivo JSON"""
    datos = context['ti'].xcom_pull(task_ids='calcular')
    
    # Guardar en archivo
    filename = f"/tmp/clima_{datetime.now().strftime('%Y%m%d')}.json"
    with open(filename, 'w') as f:
        json.dump(datos, f, indent=2)
    
    print(f"Datos guardados en {filename}")
    print(f"Contenido: {json.dumps(datos, indent=2)}")

# Definir el DAG
with DAG(
    dag_id='pipeline_clima',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@hourly',
    catchup=False,
    tags=['ejemplo', 'clima'],
    description='Pipeline que procesa datos del clima'
) as dag:
    
    extraer = PythonOperator(
        task_id='extraer',
        python_callable=extraer_clima
    )
    
    calcular = PythonOperator(
        task_id='calcular',
        python_callable=calcular_estadisticas
    )
    
    guardar = PythonOperator(
        task_id='guardar',
        python_callable=guardar_resultados
    )
    
    # Flujo
    extraer >> calcular >> guardar