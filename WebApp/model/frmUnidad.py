from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import validators
from wtforms.validators import DataRequired
class FrmUnidad(FlaskForm):
    unidad = StringField("Agregar una Unidad:",validators=[DataRequired()])