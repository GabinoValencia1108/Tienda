from flask import render_template, flash, redirect, url_for, request
from flask.blueprints import Blueprint
from sqlalchemy.orm import query
from WebApp.model.model import Nueva_SalidaTienda, ProductForm, ProveedorForm, Proveedores_Tienda, StockTienda, NuevaSalidaForm
from WebApp import db

index = Blueprint("index", __name__)

@index.route("/")
@index.route("/home")
def main_page():
    return render_template("index.html", productos=StockTienda.query.all())

# Crear productos
@index.route('/registro', methods=['GET', 'POST'])
def registro():
    form = ProductForm(meta={'csrf': False})
    #listado = [(articulo.id_producto,articulo.nombre_producto) for articulo in StockTienda.query.all()]
    # form.catalogo.choices=listado
    paquetes = StockTienda.query.filter(
        StockTienda.categoria == "paquetes").all()
    piezas = StockTienda.query.filter(StockTienda.categoria == "piezas").all()
    if form.validate_on_submit():
        producto = StockTienda(request.form['id_producto'], request.form['nombre_producto'], request.form['descripcion'],request.form['categoria'], request.form['almacen'], request.form['cantidad'])
        db.session.add(producto)
        db.session.commit()
        print(request.form.get('catalogo'))
        flash("Producto registrado exitosamente")
        return redirect(url_for('index.registro'))
    if form.errors:
        flash(form.errors, "danger")
    return render_template("alta.html", form=form, paquetes=paquetes, piezas=piezas)

# Crear salidas
@index.route('/salidas', methods=['GET', 'POST'])
def salidas():
    form = NuevaSalidaForm(meta={'csrf': False})
    if form.validate_on_submit():
        salida = StockTienda.query.filter_by(nombre_producto='libreta', id_producto=75030100920).first()
        nuevo_valor = int(salida.cantidad)
        nuevo_valor = nuevo_valor-int(request.form['cantidad'])
        actualizar = StockTienda.query.filter_by(nombre_producto='libreta', id_producto=75030100920).first()
        actualizar.cantidad = nuevo_valor
        db.session.add(actualizar)
        db.session.commit()
        producto = Nueva_SalidaTienda(request.form['id_salida'], request.form['codigo'], request.form['nombre_producto'], request.form['descripcion'],request.form['no_de_documento'], request.form['nombre_empleado'], request.form['fecha_registro'], request.form['cantidad'])
        db.session.add(producto)
        db.session.commit()
        flash("Salida con exito")
        return redirect(url_for('index.salidas'))
    if form.errors:
        flash(form.errors, "danger")
    return render_template("salidas.html", form=form)
# Crear proveedores


@index.route('/proveedores', methods=['GET', 'POST'])
def proveedores():
    form = ProveedorForm(meta={'csrf': False})
    if form.validate_on_submit():
        Producto = Proveedores_Tienda(
            request.form['id_proveedores'], request.form['nombre_proveedor'], request.form['numero_pedido'])
        db.session.add(Producto)
        db.session.commit()
        flash("Número de documento guardado")
        return redirect(url_for('index.proveedores'))
    if form.errors:
        flash(form.errors, "danger")
    return render_template("proveedor.html", form=form)
