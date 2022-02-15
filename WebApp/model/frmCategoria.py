from flask_wtf import FlaskForm
from wtforms import StringField
<<<<<<< HEAD
=======
from wtforms import validators
>>>>>>> 0c2907a5d5b52b79ad110ed80370c7436a46e41d
from wtforms.validators import DataRequired
class FrmCategoria(FlaskForm):
    categoria = StringField("Agregar una Categoría:",validators=[DataRequired()])