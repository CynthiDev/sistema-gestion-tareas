# seed.py
from werkzeug.security import generate_password_hash

def crear_datos_iniciales(db, Usuario, Tarea):
    """Crea datos de prueba si no existen"""
    if not Usuario.query.first():
        # Crear usuario de prueba
        usuario_prueba = Usuario(usuario="admin", contraseña=generate_password_hash("123"))
        db.session.add(usuario_prueba)
        db.session.commit()
        
        # Crear tareas de prueba
        tareas_iniciales = [
            Tarea(titulo="Entregar PFO2", descripcion="Enviar código y  conclusiones", usuario_id=usuario_prueba.id),
            Tarea(titulo="Estudiar Flask", descripcion="Hacer el proyecto de gestión de tareas", usuario_id=usuario_prueba.id),
            Tarea(titulo="Reunión con equipo", descripcion="Lunes 10:00 AM", usuario_id=usuario_prueba.id)
        ]
        
        for tarea in tareas_iniciales:
            db.session.add(tarea)
        db.session.commit()