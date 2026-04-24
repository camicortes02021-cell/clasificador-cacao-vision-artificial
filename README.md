# Clasificador de Calidad de Cacao con Visión Artificial

## Descripción del Proyecto

Este proyecto consiste en el desarrollo de una **aplicación de escritorio** basada en visión artificial que permite clasificar la calidad del cacao en tres categorías: **bueno, regular y malo**, a partir del análisis de imágenes.

El sistema busca apoyar a productores y evaluadores en la toma de decisiones, reduciendo la subjetividad en la clasificación manual y mejorando la calidad del producto.

---

## Contexto

El cacao en Tumaco, Nariño, es una fuente importante de ingresos para muchas familias. Sin embargo, su clasificación se realiza de forma manual, lo que puede generar inconsistencias.

Este proyecto propone una solución tecnológica basada en inteligencia artificial para modernizar este proceso.

---

## Objetivo General

Desarrollar un sistema de visión artificial que permita clasificar automáticamente la calidad del cacao mediante el análisis de imágenes digitales.

---

## Objetivos Específicos

* Diseñar una interfaz de escritorio para la carga de imágenes.
* Implementar un modelo de inteligencia artificial para clasificación.
* Almacenar los resultados en una base de datos local.
* Generar reportes de clasificación.
* Permitir la consulta del historial de resultados.

---

##  Características del Sistema

* Aplicación de escritorio (no requiere navegador).
* Interfaz gráfica amigable.
* Clasificación automática de imágenes.
* Resultados con porcentaje de confianza.
* Almacenamiento local de datos.
* Historial de clasificaciones.

---

## Arquitectura del Sistema

El sistema está compuesto por los siguientes módulos:

* **Interfaz de Usuario (UI):** desarrollada en Python utilizando PySide6, permitiendo una interfaz gráfica moderna, interactiva y multiplataforma.
* **Lógica de Aplicación:** encargada del procesamiento del flujo del sistema, gestión de eventos y control de la aplicación.
* **Módulo de Inteligencia Artificial:** responsable de la clasificación de imágenes mediante redes neuronales convolucionales (CNN).
* **Base de Datos Local:** almacenamiento de resultados utilizando SQLite integrado dentro del proyecto.

---

## Tecnologías Utilizadas

* Python
* OpenCV
* TensorFlow / Keras
* PySide6
* SQLite
* Git y GitHub
* Visual Studio Code

---

## Modelo de Inteligencia Artificial

El sistema utiliza un modelo de redes neuronales convolucionales (CNN) entrenado para clasificar imágenes de cacao en tres categorías: bueno, regular y malo.

El modelo analiza características como:

* Color del grano
* Textura
* Presencia de defectos

Esto permite una clasificación más precisa y objetiva.

---

## Base de Datos

El sistema utiliza una base de datos **local integrada** con SQLite, lo que permite que la aplicación funcione sin conexión a internet.

La base de datos se almacena dentro del proyecto como un archivo:

```
cacao.db
```

### Información almacenada:

* Fecha
* Resultado (bueno, regular, malo)
* Confianza (%)
* Ruta de la imagen

---

## Estructura del Proyecto

```
clasificador_cacao_ia/
├── app/                          # Módulo principal de la aplicación
│   ├── __init__.py               # Inicialización del paquete
│   ├── controllers/              # Controladores (lógica entre UI y servicios)
│   │   ├── __init__.py
│   │   ├── history_controller.py     # Manejo del historial de clasificaciones
│   │   └── prediction_controller.py  # Control de predicciones del modelo
│   ├── models/                   # Definición de estructuras de datos
│   │   └── __init__.py
│   ├── services/                 # Servicios del sistema (lógica de negocio)
│   │   ├── __init__.py
│   │   ├── camera_service.py         # Captura de imágenes desde cámara
│   │   ├── database_service.py       # Gestión de la base de datos SQLite
│   │   ├── image_processing_service.py # Procesamiento de imágenes
│   │   └── model_service.py          # Carga y uso del modelo de IA
│   ├── ui/                       # Interfaz gráfica (PySide6)
│   │   ├── __init__.py
│   │   ├── capture_view.py           # Vista de captura de imágenes
│   │   ├── history_view.py           # Vista del historial
│   │   ├── main_window.py            # Ventana principal
│   │   ├── reports_view.py           # Generación de reportes
│   │   ├── results_view.py           # Visualización de resultados
│   │   └── tumaco_info_view.py       # Información sobre el cacao en Tumaco
│   └── utils/                    # Utilidades y constantes del sistema
│       ├── __init__.py
│       └── constants.py              # Variables globales
│
├── assets/                       # Recursos visuales
│   ├── images/                  # Imágenes (logos, fondos)
│   └── styles/                  # Estilos (QSS)
│
├── data/                        # Datos del sistema
│   ├── database/
│   │   └── cacao.db            # Base de datos SQLite
│   ├── dataset_cacao/          # Dataset del modelo
│   ├── images/                 # Imágenes procesadas
│   ├── raw_cacao/              # Imágenes originales
│   └── samples/                # Muestras de prueba
│
├── ml/                          # Módulo de Machine Learning
│   ├── model/                   # Modelos entrenados
│   ├── split_dataset.py         # División del dataset
│   └── train_model.py           # Entrenamiento del modelo
│
├── build/                       # Archivos temporales
├── dist/                        # Ejecutable del sistema
├── env_ia/                      # Entorno virtual IA
├── envirtual/                   # Entorno virtual general
├── main.py                      # Archivo principal
├── main.spec                    # Configuración del ejecutable
├── README.md                    # Documentación
└── requirements.txt             # Dependencias
```

---

## Requisitos

* Python 3.8 o superior
* pip instalado
* Sistema operativo Windows

---

## Instalación y Ejecución

### 1. Clonar el repositorio

```
git clone https://github.com/tu-usuario/tu-repositorio.git
```

### 2. Entrar al proyecto

```
cd clasificador_cacao_ia
```

### 3. Crear entorno virtual

```
python -m venv venv
```

### 4. Activar entorno (Windows)

```
venv\Scripts\activate
```

### 5. Instalar dependencias

```
pip install -r requirements.txt
```

### 6. Ejecutar la aplicación

```
python main.py
```

---

## Funcionamiento del Sistema

1. El usuario carga una imagen de cacao.
2. El sistema procesa la imagen.
3. El modelo de IA analiza características como color y textura.
4. Se genera una clasificación:

   * Bueno
   * Regular
   * Malo
5. Se muestra el resultado con porcentaje de confianza.
6. Se almacena en la base de datos.

---

## Metodología

El proyecto se desarrolló bajo la metodología ágil **Scrum**, permitiendo una construcción iterativa e incremental.

---

## Autores

* Camila Dayana Torres
* Ronald Ariel Vargas

Universidad de Nariño
Facultad de Ingeniería
2026

---

## Futuras Mejoras

* Implementación en dispositivos móviles.
* Uso de cámara en tiempo real.
* Mejora del modelo de inteligencia artificial.
* Integración con sistemas productivos.

---

## Impacto del Proyecto

Este sistema contribuye a la modernización del sector cacaotero, mejorando la calidad del producto, reduciendo errores y facilitando la toma de decisiones.

---

## Licencia

Proyecto desarrollado con fines académicos.
