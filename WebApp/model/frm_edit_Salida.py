from flask_wtf import FlaskForm
from wtforms import StringField,DateField,SelectField
from wtforms.validators import DataRequired
class FrmEditSalida(FlaskForm):
    fecha = DateField("Fecha:", validators=[DataRequired()], format='%Y-%m-%d')
    solicita = SelectField("solicita:",validators=[DataRequired()])
    descripcion = SelectField("Descripción:",validators=[DataRequired()])
    tipo_salida = SelectField("Tipo de salida:",validators=[DataRequired()])
    cantidad = StringField("Cantidad:",validators=[DataRequired()])
    observaciones = StringField("Observaciones:",validators=[DataRequired()])
    