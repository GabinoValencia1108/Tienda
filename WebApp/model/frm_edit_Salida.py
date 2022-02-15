from flask_wtf import FlaskForm
from wtforms import StringField,DateField,SelectField
from wtforms.validators import DataRequired
class FrmEditSalida(FlaskForm):
    fecha = DateField("Fecha:", validators=[DataRequired()], format='%Y-%m-%d')
<<<<<<< HEAD
    solicita = SelectField("solicita:",validators=[DataRequired()])
    descripcion = SelectField("Descripción:",validators=[DataRequired()])
    tipo_salida = SelectField("Tipo de salida:",validators=[DataRequired()])
=======
    solicita = StringField("solicita:",validators=[DataRequired()])
    descripcion = StringField("Descripción:",validators=[DataRequired()])
    unidad = StringField("Unidad:",validators=[DataRequired()])
    tipo_ingreso = StringField("Tipo ingreso:",validators=[DataRequired()])
>>>>>>> 0c2907a5d5b52b79ad110ed80370c7436a46e41d
    cantidad = StringField("Cantidad:",validators=[DataRequired()])
    observaciones = StringField("Observaciones:",validators=[DataRequired()])
    