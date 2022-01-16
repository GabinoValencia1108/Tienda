from flask import render_template,Blueprint,flash,redirect,url_for,request
from ...model.frmCategoria import FrmCategoria
from ...model.DBCategoria import DBCategoria
from WebApp import db
categoria_bp = Blueprint("categoria_bp",__name__)
@categoria_bp.route('/categoria/',methods=['GET','POST'])
def categoria_add():
    frmCategoria = FrmCategoria(meta={'csrf': False})
    categoria = DBCategoria.query.order_by(DBCategoria.id_categoria)
    if frmCategoria.validate_on_submit():
        nuevo_ingreso = DBCategoria(frmCategoria.categoria.data)
        db.session.add(nuevo_ingreso)
        db.session.commit()
        flash("Categoría Agregado Exitosamente!")
        return redirect(url_for('categoria_bp.categoria_add'))
    if frmCategoria.errors:
        flash(frmCategoria.errors, "danger")
    return render_template("categoria.html",form = frmCategoria,categoria=categoria)
@categoria_bp.route('/editar-categoria/<int:id>',methods=['GET','POST'])
def categoria_edit(id):
    frmCategoria = FrmCategoria(meta={'csrf': False})
    categoria = DBCategoria.query.get_or_404(id)
    frmCategoria.categoria.data = categoria.categoria
    if frmCategoria.validate_on_submit():
        p_edit = DBCategoria.query.filter(DBCategoria.id_categoria == id).first()
        p_edit.categoria = request.form['categoria']
        db.session.add(p_edit)
        db.session.commit()
        flash("Categoría Editado Exitosamente!")
        return redirect(url_for('categoria_bp.categoria_add'))
    return render_template("editar_categoria.html",form = frmCategoria,categoria = categoria)
@categoria_bp.route('/eliminar-categoria/<int:id>',methods=['GET','POST'])
def categoria_del(id):
    del_categoria = DBCategoria.query.filter(DBCategoria.id_categoria == id).first()
    db.session.delete(del_categoria)
    db.session.commit()
    flash("Categoria Eliminado Exitosamente!")
    return redirect(url_for('categoria_bp.categoria_add'))