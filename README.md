# sistema-gestion-tareas
Trabajo práctico de API-REST, autenticacion con protección de contraseñas hasheadas e interacion con Base de Datos SQLite


# Sistema de Gestión de Tareas

## Estructura del proyecto
```bash
src/
├── client/ # Cliente de consola
│ └── client.py
└── server/ # Servidor Flask
├── server.py
└── requirements.txt
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

#### 4. Respuestas conceptuales:

**¿Por qué hashear contraseñas?**  
El hashing protege las contraseñas en caso de violación de datos. A diferencia del cifrado, el hash es irreversible. Al usar funciones como bcrypt o PBKDF2:
- Evitas que contraseñas queden expuestas en texto plano
- Mitigas el impacto de ataques a la base de datos
- Cumples con estándares de seguridad básicos
- Proteges a usuarios que reutilizan contraseñas

**Ventajas de SQLite en este proyecto**:
1. **Configuración cero**: No requiere servidor separado
2. **Portabilidad**: Base de datos en un solo archivo
3. **Requisitos mínimos**: Ideal para proyectos pequeños
4. **Compatibilidad**: Soporte nativo en Python
5. **Rendimiento adecuado**: Para cargas de trabajo moderadas
6. **Facilidad de backup**: Solo copiar el archivo .db




