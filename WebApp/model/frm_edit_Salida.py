from flask_wtf import FlaskForm
from wtforms import StringField,DateField,SelectField
from wtforms.validators import DataRequired
class FrmEditSalida(FlaskForm):
    fecha = DateField("Fecha:", validators=[DataRequired()], format='%Y-%m-%d')
    solicita = StringField("solicita:",validators=[DataRequired()])
    descripcion = StringField("Descripción:",validators=[DataRequired()])
    unidad = StringField("Unidad:",validators=[DataRequired()])
    tipo_ingreso = StringField("Tipo ingreso:",validators=[DataRequired()])
    cantidad = StringField("Cantidad:",validators=[DataRequired()])
    observaciones = StringField("Observaciones:",validators=[DataRequired()])
    