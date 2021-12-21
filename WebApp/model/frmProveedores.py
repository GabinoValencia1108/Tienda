from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
class FrmProveedores(FlaskForm):
    proveedor = StringField("Agregar proveedor:",validators=[DataRequired()])