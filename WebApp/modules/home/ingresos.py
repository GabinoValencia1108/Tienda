from flask import render_template,Blueprint,flash,redirect,url_for,request
<<<<<<< HEAD
from WebApp.model.DBMateriales import DBMateriales
=======
from WebApp.model.DBCategoria import DBCategoria
from WebApp.model.DBMateriales import DBMateriales

from WebApp.model.DBUnidad import DBUnidad
>>>>>>> 0c2907a5d5b52b79ad110ed80370c7436a46e41d
from ...model.frmIngresos import FrmIngresos
from ...model.frm_edit_Ingreso import FrmIngresos_edit
from datetime import datetime
from ...model.DBIngresos import DBIngresos
from ...model.DBMateriales import DBMateriales
from ...model.DBTipos import DBTipos
from WebApp import db
from flask_login import login_required
ingresos_bp = Blueprint("ingresos_bp",__name__)
@ingresos_bp.before_request
@login_required
def constructor():
    pass
@ingresos_bp.route('/ingresos/',methods=['GET','POST'])
def ingreso_add():
    frmIngresos = FrmIngresos(meta={'csrf': False})
    lista_ingresos = DBIngresos.query.order_by(DBIngresos.id_ingreso)
    list_descripcion = [(des.descripcion,des.descripcion)for des in DBMateriales.query.all()]
    tipos_ingresos = [(tipo.tipos,tipo.tipos)for tipo in DBTipos.query.all()]
    frmIngresos.tipo_ingreso.choices = tipos_ingresos
<<<<<<< HEAD
=======
    list_unidad = [(des.unidad,des.unidad)for des in DBUnidad.query.all()]
    list_categoria = [(des.categoria,des.categoria)for des in DBCategoria.query.all()]
>>>>>>> 0c2907a5d5b52b79ad110ed80370c7436a46e41d
    frmIngresos.descripcion.choices = list_descripcion
    if frmIngresos.validate_on_submit():

        aument = DBMateriales.query.filter(DBMateriales.descripcion == frmIngresos.descripcion.data).first()
        aumento_final = int(aument.stock) + (int(frmIngresos.cantidad.data))
        aument.stock=aumento_final
        db.session.add(aument)
        db.session.commit()


        nuevo_ingreso = DBIngresos(frmIngresos.fecha.data,frmIngresos.tipo_ingreso.data,frmIngresos.descripcion.data,frmIngresos.cantidad.data)
        db.session.add(nuevo_ingreso)
        db.session.commit()
        flash("Nuevo Ingreso Registrado Exitosamente!")
        return redirect(url_for('ingresos_bp.ingreso_add'))
    if frmIngresos.errors:
        flash(frmIngresos.errors, "danger")
    return render_template("ingresos.html",ingresos = lista_ingresos,form = frmIngresos)
@ingresos_bp.route('/editar-ingreso/<int:id>',methods=['GET','POST'])
def editar_ingreso(id):
    frm_ingresos_edit = FrmIngresos_edit(meta={'csrf': False})
    ingreso = DBIngresos.query.get_or_404(id)
    list_descripcion = [(des.descripcion,des.descripcion)for des in DBMateriales.query.all()]
    frm_ingresos_edit.descripcion.choices = list_descripcion
    list_ingresos = [(tipo.tipos,tipo.tipos)for tipo in DBTipos.query.all()]
    frm_ingresos_edit.tipo_ingreso.choices = list_ingresos
    fecha = ingreso.fecha
    fecha_dt = datetime.strptime(fecha, '%Y-%m-%d')
    frm_ingresos_edit.fecha.data = fecha_dt
    frm_ingresos_edit.tipo_ingreso.data = ingreso.tipo_ingreso
    frm_ingresos_edit.descripcion.data = ingreso.descripcion
    frm_ingresos_edit.cantidad.data = ingreso.cantidad
    if frm_ingresos_edit.validate_on_submit():
        nuevos_datos = DBIngresos.query.filter(DBIngresos.id_ingreso==id).first()
        nuevos_datos.fecha = request.form['fecha']
        nuevos_datos.tipo_ingreso = request.form['tipo_ingreso']
        nuevos_datos.descripcion = request.form['descripcion']
        nuevos_datos.cantidad = request.form['cantidad']
        db.session.add(nuevos_datos)
        db.session.commit()
        flash("Ingreso Editado Exitosamente")
        return redirect(url_for("ingresos_bp.ingreso_add"))
    if frm_ingresos_edit.errors:
        flash(frm_ingresos_edit.errors, "danger")
    return render_template("editar_ingreso.html",form = frm_ingresos_edit)
@ingresos_bp.route('/eliminar-ingreso/<int:id>')
def eliminar(id):
    ingreso_eliminar =DBIngresos.query.filter(DBIngresos.id_ingreso==id).first()
    db.session.delete(ingreso_eliminar)
    db.session.commit()
    flash("Ingreso Eliminado Exitosamente!")
    return redirect(url_for("ingresos_bp.ingreso_add"))