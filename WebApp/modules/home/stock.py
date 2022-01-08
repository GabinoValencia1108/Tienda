from flask import render_template,Blueprint,flash,redirect,url_for,request
from ...model.frmStock import FrmStock
from ...model.DBStock import DBStock
from WebApp import db
stock_bp = Blueprint("stock_bp",__name__)
@stock_bp.route('/stock/',methods=['GET','POST'])
def stock_add():
    frmStock = FrmStock(meta={'csrf': False})
    stock = DBStock.query.order_by(DBStock.id_stock)
    if frmStock.validate_on_submit():
        nuevo_ingreso = DBStock(frmStock.descripcion.data,frmStock.unidad.data,frmStock.categoria.data,frmStock.stock.data)
        db.session.add(nuevo_ingreso)
        db.session.commit()
        flash("Producto Agregado Exitosamente!")
        return redirect(url_for('stock_bp.stock_add'))
    if frmStock.errors:
        flash(frmStock.errors, "danger")
    return render_template("stock.html",form = frmStock,stock=stock)
@stock_bp.route('/editar-stock/<int:id>',methods=['GET','POST'])
def stock_edit(id):
    frmStock = FrmStock(meta={'csrf': False})
    stock = DBStock.query.get_or_404(id)
    frmStock.descripcion.data = stock.descripcion
    frmStock.unidad.data = stock.unidad
    frmStock.categoria.data = stock.categoria
    if frmStock.validate_on_submit():
        p_edit = DBStock.query.filter(DBStock.id_stock == id).first()
        p_edit.descripcion = request.form['descripcion']
        p_edit.unidad = request.form['unidad']
        p_edit.categoria = request.form['categoria']
        db.session.add(p_edit)
        db.session.commit()
        flash("Catalogo Editado Exitosamente!")
        return redirect(url_for('stock_bp.stock_add'))
    return render_template("editar_stock.html",form = frmStock,stock = stock)
@stock_bp.route('/eliminar-stock/<int:id>',methods=['GET','POST'])
def stock_del(id):
    del_stock = DBStock.query.filter(DBStock.id_stock == id).first()
    db.session.delete(del_stock)
    db.session.commit()
    flash("Producto Eliminado Exisotsamente!")
    return redirect(url_for('stock_bp.stock_add'))