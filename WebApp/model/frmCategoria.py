from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import validators
from wtforms.validators import DataRequired
class FrmCategoria(FlaskForm):
    categoria = StringField("Agregar una Categoría:",validators=[DataRequired()])