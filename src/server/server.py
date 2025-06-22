from flask import Flask, request, jsonify, make_response, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
# Ubicación de DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tareas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'clave_secreta_segura'  #se usa para firmar digitalmente estas cookies
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',  # Permite enviar cookies en peticiones GET
    SESSION_COOKIE_PATH='/',
    SESSION_COOKIE_SECURE=False  # True en producción con HTTPS
)
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50), unique=True, nullable=False)
    contraseña = db.Column(db.String(100), nullable=False)

class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(200))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)



# Importar seed DESPUÉS de definir los modelos
from seed import crear_datos_iniciales




@app.route('/registro', methods=['POST'])
def registro():
    datos = request.get_json()
    usuario = datos.get('usuario')
    contraseña = datos.get('contraseña')
    
    if not usuario or not contraseña:
        return jsonify({'error': 'Faltan datos'}), 400
    
    if Usuario.query.filter_by(usuario=usuario).first():
        return jsonify({'error': 'Usuario ya existe'}), 400
    
    hashed_pw = generate_password_hash(contraseña)
    nuevo_usuario = Usuario(usuario=usuario, contraseña=hashed_pw)
    db.session.add(nuevo_usuario)
    db.session.commit()
    
    return jsonify({'mensaje': 'Usuario creado exitosamente'}), 201





@app.route('/login', methods=['POST'])
def login():
    datos = request.get_json()
    usuario = datos.get('usuario')
    contraseña = datos.get('contraseña')
    
    usuario_existente = Usuario.query.filter_by(usuario=usuario).first()
    
    if not usuario_existente or not check_password_hash(usuario_existente.contraseña, contraseña):
        return jsonify({'error': 'Credenciales inválidas'}), 401
    
    # ESTABLECER SESIÓN - PARTE CLAVE
    session['usuario_id'] = usuario_existente.id
    
    return jsonify({
        'mensaje': 'Inicio de sesión exitoso',
        'usuario_id': usuario_existente.id
    }), 200



@app.route('/logout', methods=['POST'])
def logout():
    session.pop('usuario_id', None)
    return jsonify({'mensaje': 'Sesión cerrada exitosamente'}), 200




@app.route('/tareas', methods=['GET'])
def obtener_tareas():
    # Verificar si el usuario ha iniciado sesión, La verificación depende de la firma
    if 'usuario_id' not in session:
        print("Acceso no autorizado: sesión no encontrada")
        return jsonify({'error': 'Acceso no autorizado'}), 401
    
    # Para depuración: muestra el ID de sesión
    print(f"Sesión activa para usuario: {session['usuario_id']}")

    # Obtener usuario actual
    usuario_actual = db.session.get(Usuario, session['usuario_id'])
    
    # Obtener tareas del usuario
    tareas = Tarea.query.filter_by(usuario_id=usuario_actual.id).all()
    
    # Generar HTML con las tareas
    html = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Sistema de Gestión de Tareas</title>
    </head>
    <body>
        <h1>¡Bienvenido {usuario_actual.usuario}!</h1>
        <h2>Tus tareas:</h2>
        <ul>
    '''

    if not tareas:
        html += '<li>No tienes tareas registradas</li>'
    else:
        for tarea in tareas:
            html += f'<li><strong>{tarea.titulo}</strong>: {tarea.descripcion}</li>'        
    
    html += '''
        </ul>
    </body>
    </html>
    '''
    return html





@app.route('/tareas', methods=['POST'])
def crear_tarea():
    if 'usuario_id' not in session:
        return jsonify({'error': 'Acceso no autorizado'}), 401
    
    datos = request.get_json()
    titulo = datos.get('titulo')
    descripcion = datos.get('descripcion', '')
    
    if not titulo:
        return jsonify({'error': 'Título es requerido'}), 400
    
    nueva_tarea = Tarea(
        titulo=titulo,
        descripcion=descripcion,
        usuario_id=session['usuario_id']
    )
    
    db.session.add(nueva_tarea)
    db.session.commit()
    
    return jsonify({
        'mensaje': 'Tarea creada exitosamente',
        'tarea': {
            'id': nueva_tarea.id,
            'titulo': nueva_tarea.titulo,
            'descripcion': nueva_tarea.descripcion
        }
    }), 201



# Crear tablas al inicio
with app.app_context():
    db.create_all()
    crear_datos_iniciales(db, Usuario, Tarea)  # Pasar los modelos como argumentos





if __name__ == '__main__':
    app.run(debug=True)