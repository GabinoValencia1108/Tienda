from WebApp.modules.iniciar.login_user import blue_login
from WebApp.modules.home.index import index
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
app = Flask(__name__)

app.config.from_object("configuration.DevelopmentConfig")

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "blue_login.login"

app.register_blueprint(index)
app.register_blueprint(blue_login)
db.create_all()
