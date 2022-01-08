from flask_wtf import FlaskForm
from wtforms import StringField,DateField
from wtforms import validators
from wtforms.validators import DataRequired
class FrmStock(FlaskForm):
    descripcion = StringField("Descripción:",validators=[DataRequired()])
    unidad = StringField("Unidad:",validators=[DataRequired()])
    categoria = StringField("Categoría:",validators=[DataRequired()])
    stock = StringField("Stock:",validators=[DataRequired()])