# sistema-gestion-tareas
Trabajo práctico de API-REST, autenticacion con protección de contraseñas hasheadas e interacion con Base de Datos SQLite


## Estructura del proyecto
```bash
sistema-gestion-tareas/
├── src/
│   ├── client/
│       ├── client.py # Cliente de consola
│   │   └── requirements.txt  
│   └── server/
│       ├── server.py  # Servidor Flask
│       ├── requirements.txt
│       └── seed.py
├── docs/
│   ├── index.html  # GitHub Pages
│   └── screenshots/
├── .gitignore
└── README.md
```

## Instrucciones de ejecución
### Requisitos
- Python 3.8+
- Dependencias: `pip install -r requirements.txt`

### Ejecución

1. Iniciar servidor:
```bash
#Posicionarse en Server: 
cd src/server

#Instalar dependencias: 
pip install -r requirements.txt

#Iniciar el Servidor, La base de datos `tareas.db` se creará automáticamente: 
python server.py
```


2. Iniciar cliente en otra terminal:
```bash
#Posicionarse en client: 
cd src/client

#Instalar dependencias: 
pip install -r requirements.txt

#Iniciar el Cliente: 
python client.py
```

### Shorcuts
1. Inicia el servidor: `python src/server/server.py`
2. Inicia el cliente: `python src/client/client.py`
3. Sigue las instrucciones en el cliente

#### Uso del cliente 
Probar con cURL o Postman 
- Registrarse: Crea un nuevo usuario
- Iniciar sesión: Valida tus credenciales
- Ver tareas: Muestra la página de bienvenida
- Salir: Termina la aplicación

#### Endpoints de la API
- POST /registro: Registra un nuevo usuario
- POST /login: Inicia sesión
- GET /tareas: Devuelve HTML de bienvenida





