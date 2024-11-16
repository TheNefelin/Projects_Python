from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("BD_CONN_MYSQL")

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Roll(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nombre = db.Column(db.String(255))

class Usuario(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nombre = db.Column(db.String(255))
  id_roll = db.Column(db.Integer, db.ForeignKey('roll.id'))

  roll = db.relationship('Roll', back_populates='usuarios')

Roll.usuarios = db.relationship('Usuario', back_populates='roll')

with app.app_context():
  db.drop_all() #--- Solo si nececitas limpiar la base de datos ---
  db.create_all()

  roll_admin = Roll(nombre='Administrador')
  roll_user = Roll(nombre='Usuario')

  db.session.add_all([
    roll_admin,
    roll_user
  ])

  db.session.commit()

  db.session.add_all([
    Usuario(nombre='Superman', roll=roll_admin),
    Usuario(nombre='Batman', roll=roll_user),
    Usuario(nombre='Wonder Woman', roll=roll_user),
    Usuario(nombre='Acuaman', roll=roll_user),
  ])

  db.session.commit()


