from flask import render_template,Blueprint,flash,redirect,url_for,request
from ...model.frmMateriales import FrmMateriales
from ...model.DBMateriales import DBMateriales
from ...model.frm_edit_Materiales import FrmEditMateriales 
from WebApp.model.DBCategoria import DBCategoria
from WebApp.model.DBUnidad import DBUnidad
from flask_login import login_required
from WebApp import db
materiales_bp = Blueprint("materiales_bp",__name__)
@materiales_bp.before_request
@login_required
def constructor():
    pass
@materiales_bp.route('/materiales/',methods=['GET','POST'])
def materiales_add():
    frmMateriales = FrmMateriales(meta={'csrf': False})
    materiales = DBMateriales.query.order_by(DBMateriales.id_materiales)
    list_unidad = [(des.unidad,des.unidad)for des in DBUnidad.query.all()]
    list_categoria = [(des.categoria,des.categoria)for des in DBCategoria.query.all()]
    frmMateriales.unidad.choices = list_unidad
    frmMateriales.categoria.choices = list_categoria
    if frmMateriales.validate_on_submit():
        nuevo_ingreso = DBMateriales(frmMateriales.descripcion.data,frmMateriales.unidad.data,frmMateriales.categoria.data,frmMateriales.stock.data)
        db.session.add(nuevo_ingreso)
        db.session.commit()
        flash("Articulo Agregado Exitosamente!")
        return redirect(url_for('materiales_bp.materiales_add'))
    if frmMateriales.errors:
        flash(frmMateriales.errors, "danger")
    return render_template("materiales.html",form = frmMateriales,materiales=materiales)
@materiales_bp.route('/editar-materiales/<int:id>',methods=['GET','POST'])
def materiales_edit(id):
    frm_edit_materiales = FrmEditMateriales(meta={'csrf': False})
    materiales = DBMateriales.query.get_or_404(id)
    list_descripcion = [(des.descripcion,des.descripcion)for des in DBMateriales.query.all()]
    frm_edit_materiales.descripcion.choices = list_descripcion
    list_unidad = [(uni.unidad,uni.unidad)for uni in DBUnidad.query.all()]
    frm_edit_materiales.unidad.choices = list_unidad
    list_categoria = [(categ.categoria,categ.categoria)for categ in DBCategoria.query.all()]
    frm_edit_materiales.categoria.choices = list_categoria
    frm_edit_materiales.descripcion.data = materiales.descripcion
    frm_edit_materiales.unidad.data = materiales.unidad
    frm_edit_materiales.categoria.data = materiales.categoria
    frm_edit_materiales.stock.data = materiales.stock
    if frm_edit_materiales.validate_on_submit():
        p_edit = DBMateriales.query.filter(DBMateriales.id_materiales == id).first()
        p_edit.descripcion = request.form['descripcion']
        db.session.add(p_edit)
        db.session.commit()
        flash("Articulo Editado Exitosamente!")
        return redirect(url_for('materiales_bp.materiales_add'))
    return render_template("editar_materiales.html",form = frm_edit_materiales,materiales = materiales)
@materiales_bp.route('/eliminar-materiales/<int:id>',methods=['GET','POST'])
def materiales_del(id):
    del_materiales = DBMateriales.query.filter(DBMateriales.id_materiales == id).first()
    db.session.delete(del_materiales)
    db.session.commit()
    flash("Articulo Eliminado Exitosamente!")
    return redirect(url_for('materiales_bp.materiales_add'))