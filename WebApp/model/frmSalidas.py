from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField,DateField,SelectField,TextAreaField
from wtforms.validators import DataRequired
class FrmSalidas(FlaskForm):
    fecha = DateField("Fecha:", validators=[DataRequired()], format='%Y-%m-%d')
    solicita = SelectField("solicita:", coerce = str)
    descripcion = SelectField("Descripción:",validators=[DataRequired()])
<<<<<<< HEAD
    tipo_salida = SelectField("Tipo de salida:",validators=[DataRequired()])
    cantidad = StringField("Cantidad:",validators=[DataRequired()])
    observaciones = StringField("Observaciónes:",validators=[DataRequired()])
    agregar = TextAreaField(u'Productos seleccionados',)
=======
    unidad = SelectField("Unidad:",validators=[DataRequired()])
    tipo_ingreso = SelectField("Tipo ingreso:",validators=[DataRequired()])
    cantidad = StringField("Cantidad:",validators=[DataRequired()])
    observaciones = StringField("Observaciónes:",validators=[DataRequired()])
    categoria = SelectField("Categoria:", coerce = str)
>>>>>>> 0c2907a5d5b52b79ad110ed80370c7436a46e41d
