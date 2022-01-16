from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import validators
from wtforms.validators import DataRequired
class FrmMateriales(FlaskForm):
    descripcion = StringField("Descripción:",validators=[DataRequired()])