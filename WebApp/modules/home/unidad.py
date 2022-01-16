from flask import render_template,Blueprint,flash,redirect,url_for,request
from ...model.frmUnidad import FrmUnidad
from ...model.DBUnidad import DBUnidad
from WebApp import db
unidad_bp = Blueprint("unidad_bp",__name__)
@unidad_bp.route('/unidad/',methods=['GET','POST'])
def unidad_add():
    frmUnidad = FrmUnidad(meta={'csrf': False})
    unidad = DBUnidad.query.order_by(DBUnidad.id_unidad)
    if frmUnidad.validate_on_submit():
        nuevo_ingreso = DBUnidad(frmUnidad.unidad.data)
        db.session.add(nuevo_ingreso)
        db.session.commit()
        flash("Unidad Agregado Exitosamente!")
        return redirect(url_for('unidad_bp.unidad_add'))
    if frmUnidad.errors:
        flash(frmUnidad.errors, "danger")
    return render_template("unidad.html",form = frmUnidad,unidad=unidad)
@unidad_bp.route('/editar-unidad/<int:id>',methods=['GET','POST'])
def unidad_edit(id):
    frmUnidad = FrmUnidad(meta={'csrf': False})
    unidad = DBUnidad.query.get_or_404(id)
    frmUnidad.unidad.data = unidad.unidad
    if frmUnidad.validate_on_submit():
        p_edit = DBUnidad.query.filter(DBUnidad.id_unidad == id).first()
        p_edit.unidad = request.form['unidad']
        db.session.add(p_edit)
        db.session.commit()
        flash("Unidad Editado Exitosamente!")
        return redirect(url_for('unidad_bp.unidad_add'))
    return render_template("editar_unidad.html",form = frmUnidad,unidad = unidad)
@unidad_bp.route('/eliminar-unidad/<int:id>',methods=['GET','POST'])
def unidad_del(id):
    del_unidad = DBUnidad.query.filter(DBUnidad.id_unidad == id).first()
    db.session.delete(del_unidad)
    db.session.commit()
    flash("Unidad Eliminado Exitosamente!")
    return redirect(url_for('unidad_bp.unidad_add'))