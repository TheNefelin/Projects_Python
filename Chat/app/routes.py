from flask import render_template
from app import app, db, socketio
from app.models import Mensaje

@app.route('/')
def index():
    mensajes = Mensaje.query.all()
    return render_template('index.html', mensajes=mensajes)


from flask_socketio import emit

@socketio.on('mensaje')
def handle_mensaje(data):
    contenido = data['contenido']
    nuevo_mensaje = Mensaje(contenido=contenido)
    db.session.add(nuevo_mensaje)
    db.session.commit()
    emit('mensaje', {'contenido': contenido}, broadcast=True)