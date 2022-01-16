from flask import render_template,Blueprint,flash,redirect,url_for,request
from ...model.frmMateriales import FrmMateriales
from ...model.DBMateriales import DBMateriales
from WebApp import db
materiales_bp = Blueprint("materiales_bp",__name__)
@materiales_bp.route('/materiales/',methods=['GET','POST'])
def materiales_add():
    frmMateriales = FrmMateriales(meta={'csrf': False})
    materiales = DBMateriales.query.order_by(DBMateriales.id_materiales)
    if frmMateriales.validate_on_submit():
        nuevo_ingreso = DBMateriales(frmMateriales.descripcion.data)
        db.session.add(nuevo_ingreso)
        db.session.commit()
        flash("Articulo Agregado Exitosamente!")
        return redirect(url_for('materiales_bp.materiales_add'))
    if frmMateriales.errors:
        flash(frmMateriales.errors, "danger")
    return render_template("materiales.html",form = frmMateriales,materiales=materiales)
@materiales_bp.route('/editar-materiales/<int:id>',methods=['GET','POST'])
def materiales_edit(id):
    frmMateriales = FrmMateriales(meta={'csrf': False})
    materiales = DBMateriales.query.get_or_404(id)
    frmMateriales.descripcion.data = materiales.descripcion
    if frmMateriales.validate_on_submit():
        p_edit = DBMateriales.query.filter(DBMateriales.id_materiales == id).first()
        p_edit.descripcion = request.form['descripcion']
        db.session.add(p_edit)
        db.session.commit()
        flash("Articulo Editado Exitosamente!")
        return redirect(url_for('materiales_bp.materiales_add'))
    return render_template("editar_materiales.html",form = frmMateriales,materiales = materiales)
@materiales_bp.route('/eliminar-materiales/<int:id>',methods=['GET','POST'])
def materiales_del(id):
    del_materiales = DBMateriales.query.filter(DBMateriales.id_materiales == id).first()
    db.session.delete(del_materiales)
    db.session.commit()
    flash("Articulo Eliminado Exitosamente!")
    return redirect(url_for('materiales_bp.materiales_add'))
    