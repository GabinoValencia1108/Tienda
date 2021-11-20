from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, PasswordField,HiddenField
from werkzeug.security import check_password_hash, generate_password_hash
from wtforms.validators import EqualTo, InputRequired
from sqlalchemy import Enum
import enum
from WebApp import db
class RolUsuario(enum.Enum):
    usuario_regular = 1
class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    pwhash = db.Column(db.String(255))
    rol = db.Column(Enum(RolUsuario))

    def __init__(self, username, pwhash, rol=RolUsuario.usuario_regular):
        self.username = username
        self.pwhash = generate_password_hash(pwhash)
        self.rol = rol

    def __repr__(self):
        return "<Usuario %r>" % (self.username)

    def get_id(self):
        return str(self.id)

    def check_password(self, password):
        return check_password_hash(self.pwhash, password)

    @property
    def is_authenticated(self):
        """The foo property."""
        return True

    @property
    def is_active(self):
        """The foo property."""
        return True

    @property
    def is_anonymous(self):
        """The foo property."""
        return False
class Iniciar(FlaskForm):
    Usuario = StringField("Usuario", validators=[InputRequired()])
    contrasena = PasswordField("Password", validators=[InputRequired()])
    next = HiddenField("next")
class Registrar(FlaskForm):
    Usuario = StringField("usuario", validators=[InputRequired()])
    contrasena = PasswordField("contraseña", validators=[InputRequired(), EqualTo('confirmar_contrasena')])
    confirmar_contrasena = PasswordField('Confirmar contraseña', validators=[InputRequired()])
