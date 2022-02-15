from flask import render_template,Blueprint,flash,redirect,url_for,request
from ...model.frmTipos import FrmTipos
from ...model.DBTipos import DBTipos
from flask_login import login_required
from WebApp import db
tipos_bp = Blueprint("tipos_bp",__name__)
@tipos_bp.before_request
@login_required
def constructor():
    pass
@tipos_bp.route('/tipos',methods=['GET','POST'])
def tipos_add():
    frmTipos = FrmTipos(meta={'csrf': False})
    tipos = DBTipos.query.order_by(DBTipos.id_tipos)
    if frmTipos.validate_on_submit():
        nuevo_tipos = DBTipos(frmTipos.tipos.data,frmTipos.tipos_salida.data)
        db.session.add(nuevo_tipos)
        db.session.commit()
        flash("Tipos de ingreso registrado Exitosamente!")
        return redirect(url_for('tipos_bp.tipos_add'))
    if frmTipos.errors:
        flash(frmTipos.errors, "danger")
    return render_template("tipos.html",form=frmTipos,tipos = tipos)
@tipos_bp.route('/editar-tipos/<int:id>',methods=['GET','POST'])
def tipos_edit(id):
    tipos=DBTipos.query.get_or_404(id)
    frmTipos = FrmTipos(meta={'csrf': False})
    frmTipos.tipos.data = tipos.tipos
    frmTipos.tipos_salida.data = tipos.tipos_salida
    if frmTipos.validate_on_submit():
        p_edit = DBTipos.query.filter(DBTipos.id_tipos == id).first()
        p_edit.tipos = request.form['tipos']
        p_edit.tipos_salida = request.form['tipos_salida']
        db.session.add(p_edit)
        db.session.commit()
        flash("Tipos de ingresos Editado Exitosamente!")
        return redirect(url_for('tipos_bp.tipos_add'))
    return render_template("editar_tipos.html",form = frmTipos,tipos=tipos)
@tipos_bp.route('/eliminar-tipos/<int:id>',methods=['GET','POST'])
def producto_del(id):
    del_tipos = DBTipos.query.filter(DBTipos.id_tipos == id).first()
    db.session.delete(del_tipos)
    db.session.commit()
    flash("Tipos de ingreso Eliminado Exitosamente!")
    return redirect(url_for('tipos_bp.tipos_add'))