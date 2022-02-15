from flask_wtf import FlaskForm
from wtforms import StringField,DateField,SelectField
from wtforms.validators import DataRequired
class FrmIngresos_edit(FlaskForm):
    fecha = DateField("Fecha:", validators=[DataRequired()], format='%Y-%m-%d')
    tipo_ingreso = SelectField("Tipo ingreso:",validators=[DataRequired()],render_kw={'readonly': True})
    descripcion = SelectField("Descripción:",validators=[DataRequired()],render_kw={'readonly': True})
    cantidad = StringField("Cantidad:",validators=[DataRequired()])