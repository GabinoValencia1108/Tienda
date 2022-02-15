from flask import render_template
from flask.blueprints import Blueprint
from flask_login import login_required

index = Blueprint("index", __name__)
@index.before_request
@login_required
def constructor():
    pass
@index.route("/")
def main_page():
    return render_template("index.html")