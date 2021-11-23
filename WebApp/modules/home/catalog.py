from flask import render_template, flash, redirect, url_for, request
from flask.blueprints import Blueprint
from flask_login import login_required
from WebApp.model.model import Nueva_SalidaTienda, ProductForm, ProveedorForm, Proveedores_Tienda, StockTienda, NuevaSalidaForm
from WebApp.model.catalog import FrmCatalogo,Catalogo
from WebApp import db
alta_catalogo = Blueprint("alta_catalogo", __name__)
@alta_catalogo.before_request
@login_required
def constructor():
    pass
@alta_catalogo.route("/nuevo_catalogo", methods=['GET', 'POST'])
def registrar_catalogo():
    form = FrmCatalogo(meta={'csrf': False})
    #piezas = StockTienda.query.filter(StockTienda.categoria == "piezas").all()
    if form.validate_on_submit():
        catalogo_nombre = Catalogo(form.nuevo_catalogo.data)
        db.session.add(catalogo_nombre)
        db.session.commit()
        flash("El producto se agrego al catalogo exitosamente")
        return redirect(url_for('alta_catalogo.registrar_catalogo'))
    if form.errors:
        flash(form.errors, "danger")
    return render_template("catalogo.html", form=form)