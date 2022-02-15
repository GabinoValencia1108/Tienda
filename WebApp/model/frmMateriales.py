from flask_wtf import FlaskForm
<<<<<<< HEAD
from wtforms import StringField,SelectField
from wtforms import validators
from wtforms.validators import DataRequired
class FrmMateriales(FlaskForm):
    descripcion = StringField("Descripción:",validators=[DataRequired()])
    unidad = SelectField("Unidad:",validators=[DataRequired()])
    categoria = SelectField("Categoría:",validators=[DataRequired()])
    stock = StringField("Stock:",validators=[DataRequired()])
=======
from wtforms import StringField
from wtforms import validators
from wtforms.validators import DataRequired
class FrmMateriales(FlaskForm):
    descripcion = StringField("Descripción:",validators=[DataRequired()])
>>>>>>> 0c2907a5d5b52b79ad110ed80370c7436a46e41d
