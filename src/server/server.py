from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
# Ubicación de DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tareas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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

# Crear tablas al inicio
with app.app_context():
    db.create_all()

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
    
    return jsonify({'mensaje': 'Inicio de sesión exitoso'}), 200

@app.route('/tareas', methods=['GET'])
def obtener_tareas():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Sistema de Gestión de Tareas</title>
    </head>
    <body>
        <h1>¡Bienvenido al Sistema de Gestión de Tareas!</h1>
        <p>API funcionando correctamente</p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)