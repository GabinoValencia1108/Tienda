from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField,DateField,SelectField,TextAreaField
from wtforms.validators import DataRequired
class FrmSalidas(FlaskForm):
    fecha = DateField("Fecha:", validators=[DataRequired()], format='%Y-%m-%d')
    solicita = SelectField("solicita:", coerce = str)
    descripcion = SelectField("Descripción:",validators=[DataRequired()])
    tipo_salida = SelectField("Tipo de salida:",validators=[DataRequired()])
    cantidad = StringField("Cantidad:",validators=[DataRequired()])
    observaciones = StringField("Observaciónes:",validators=[DataRequired()])
    agregar = TextAreaField(u'Productos seleccionados',)
