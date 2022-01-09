from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
class FrmTipos(FlaskForm):
    tipos = StringField("Agregar Tipos de Ingresos:",validators=[DataRequired()])