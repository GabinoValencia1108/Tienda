from flask_wtf import FlaskForm
from wtforms import StringField,SelectField
from wtforms import validators
from wtforms.validators import DataRequired
class FrmMateriales(FlaskForm):
    descripcion = StringField("Descripción:",validators=[DataRequired()])
    unidad = SelectField("Unidad:",validators=[DataRequired()])
    categoria = SelectField("Categoría:",validators=[DataRequired()])
    stock = StringField("Stock:",validators=[DataRequired()])