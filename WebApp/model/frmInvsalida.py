from flask_wtf import FlaskForm
from wtforms import DateField
from wtforms.validators import DataRequired
class FrmInvsalida(FlaskForm):
    fecha_inicio = DateField("fecha inicio:", validators=[DataRequired()], format='%Y-%m-%d')
    fecha_fin = DateField("fecha fin:", validators=[DataRequired()], format='%Y-%m-%d')

