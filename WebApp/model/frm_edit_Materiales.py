from flask_wtf import FlaskForm
from wtforms import StringField,DateField,SelectField
from wtforms.validators import DataRequired
class FrmEditMateriales(FlaskForm):
    descripcion = SelectField("Descripción:",validators=[DataRequired()])
    unidad = SelectField("Unidad:",validators=[DataRequired()])
    categoria = SelectField("Categoría:",validators=[DataRequired()])
    stock = StringField("Existencias:",validators=[DataRequired()])
    