from flask_wtf import FlaskForm
from wtforms import DateField
from wtforms.validators import DataRequired
class FrmInventario(FlaskForm):
    fecha_inicio = DateField("Fecha inicio:", validators=[DataRequired()], format='%Y-%m-%d')
    fecha_fin = DateField("Fecha fin:", validators=[DataRequired()], format='%Y-%m-%d')