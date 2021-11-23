from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, PasswordField,HiddenField
from werkzeug.security import check_password_hash, generate_password_hash
from wtforms.validators import EqualTo, InputRequired
from sqlalchemy import Enum
from WebApp import db
class Catalogo(db.Model):
    __tablename__="catalogo"
    nombre_catalogo = db.Column(db.String(255),primary_key=True)
    def __init__(self, nombre_catalogo):
        self.nombre_catalogo = nombre_catalogo
    def __repr__(self):
        return "<catalogo %r>" % (self.nombre_catalogo)
class FrmCatalogo(FlaskForm):
    nuevo_catalogo = StringField("Nombre del producto:", validators=[InputRequired()])