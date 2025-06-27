# Sistema de Gestión de Tareas (Cliente-Servidor)

Una implementación completa de una aplicación cliente-servidor que expone una API REST para la gestión de tareas, con autenticación segura por sesiones y persistencia en una base de datos SQLite.

[![Documentación](https://img.shields.io/badge/Documentación-Ver%20en%20GitHub%20Pages-blue.svg)](https://cynthidev.github.io/sistema-gestion-tareas/)


---

## Características Principales

*   **API RESTful:** Backend construido con Flask que sigue los principios REST.
*   **Autenticación Segura:**
    *   Registro de usuarios con contraseñas hasheadas (`werkzeug.security`).
    *   Gestión de sesiones mediante cookies seguras.
*   **Persistencia de Datos:** Uso de SQLAlchemy como ORM para interactuar con una base de datos SQLite.
*   **Cliente Interactivo:** Aplicación de consola en Python para interactuar con la API de forma sencilla.
*   **Documentación Completa:** Página de documentación detallada alojada en GitHub Pages.

## Tecnologías Utilizadas

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0-black?style=for-the-badge&logo=flask&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.4-orange?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3-blue?style=for-the-badge&logo=sqlite&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-2.28-brightgreen?style=for-the-badge)

## Instalación y ejecución

Sigue estos pasos para configurar y ejecutar el proyecto en tu entorno local.

### Prerrequisitos

*   Python 3.10 o superior.
*   `pip` (gestor de paquetes de Python).

### Instalación y Ejecución

1.  **Clona el repositorio:**

    ```bash
    git clone https://github.com/cynthidev/sistema-gestion-tareas.git
    cd sistema-gestion-tareas
    ```

2.  **Configura y ejecuta el Servidor:**
    *Abre una terminal.*

    ```bash
    # 1. Navega al directorio del servidor
    cd src/server

    # 2. Instala las dependencias
    pip install -r requirements.txt

    # 3. Inicia el servidor Flask
    # La API estará disponible en http://localhost:5000
    python server.py
    ```

3.  **Configura y ejecuta el Cliente:**
    *Abre una **nueva terminal** (deja la del servidor corriendo).*

    ```bash
    # 1. Navega al directorio del cliente (desde la raíz del proyecto)
    cd src/client

    # 2. Instala las dependencias
    pip install -r requirements.txt

    # 3. Inicia el cliente interactivo
    python client.py
    ```

4.  **¡Listo!** Sigue las instrucciones que aparecen en la consola del cliente para registrarte, iniciar sesión y gestionar tus tareas.

##  Estructura del Proyecto
```bash
sistema-gestion-tareas/
├── docs/
│ ├── index.html   # GitHub Pages
│ └── screenshots/ 
├── src/
│   ├── client/
│       ├── client.py # Cliente de consola
│   │   └── requirements.txt  
│   └── server/
│       ├── server.py  # Servidor Flask
│       ├── requirements.txt
│       └── seed.py
├── .gitignore
└── README.md
```




## Autora

*   **Cynthia Estefania Choque Galindo** - [cynthidev](https://github.com/cynthidev)


