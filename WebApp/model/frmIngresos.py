from flask_wtf import FlaskForm
from wtforms import StringField,DateField,SelectField
from wtforms.validators import DataRequired
class FrmIngresos(FlaskForm):
    fecha = DateField("Fecha:", validators=[DataRequired()], format='%Y-%m-%d')
    tipo_ingreso = SelectField("Tipo ingreso:",validators=[DataRequired()])
    descripcion = SelectField("Descripción:",validators=[DataRequired()],coerce=str)
    cantidad = StringField("Cantidad:",validators=[DataRequired()])