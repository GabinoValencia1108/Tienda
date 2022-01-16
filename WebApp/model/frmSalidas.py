from flask_wtf import FlaskForm
from wtforms import StringField,DateField,SelectField
from wtforms.validators import DataRequired
class FrmSalidas(FlaskForm):
    fecha = DateField("Fecha:", validators=[DataRequired()], format='%Y-%m-%d')
    solicita = SelectField("solicita:", coerce = str)
    descripcion = SelectField("Descripción:",validators=[DataRequired()])
    unidad = SelectField("Unidad:",validators=[DataRequired()])
    tipo_ingreso = SelectField("Tipo ingreso:",validators=[DataRequired()])
    cantidad = StringField("Cantidad:",validators=[DataRequired()])
    observaciones = StringField("Observaciónes:",validators=[DataRequired()])
    categoria = SelectField("Categoria:", coerce = str)