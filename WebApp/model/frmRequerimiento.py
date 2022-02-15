from flask_wtf import FlaskForm
from wtforms import StringField,DateField,SelectField
from wtforms.validators import DataRequired
class FrmRequerimiento(FlaskForm):
    fecha = DateField("Fecha:", validators=[DataRequired()], format='%Y-%m-%d')
    partida = SelectField("Partida:",validators=[DataRequired()])
    cantidad = SelectField("Cantidad:",validators=[DataRequired()],coerce=str)
    unidad = SelectField("Unidad:",validators=[DataRequired()],coerce=str)
    descripcion = SelectField("Descripción:",validators=[DataRequired()],coerce=str)