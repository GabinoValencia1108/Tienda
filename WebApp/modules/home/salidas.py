from flask import render_template,Blueprint,flash,redirect,url_for,request
from flask_login import current_user
from datetime import datetime
from WebApp.model.DBIngresos import DBIngresos
from WebApp.model.DBUnidad import DBUnidad
from ...model.frmSalidas import FrmSalidas
from ...model.DBSalidas import DBSalidas
from ...model.DBEmpleados import DBEmpleados
from ...model.DBMateriales import DBMateriales
from ...model.DBTipos import DBTipos
from ...model.frm_edit_Salida import FrmEditSalida
from WebApp import db
salidas_bp = Blueprint("salidas_bp",__name__)
@salidas_bp.route('/salidas/',methods=['GET','POST'])
def salidas_add():
    frmSalidas = FrmSalidas(meta={'csrf': False})
    list_empleado = [(empleado.nombre_empleado,empleado.nombre_empleado)for empleado in DBEmpleados.query.all()]
    frmSalidas.solicita.choices = list_empleado
    list_descripcion = [(des.descripcion,des.descripcion)for des in DBMateriales.query.all()]
    frmSalidas.descripcion.choices = list_descripcion
    lista_unidad = [(unidad.unidad,unidad.unidad)for unidad in DBUnidad.query.all()]
    frmSalidas.unidad.choices = lista_unidad
    tipos_ingresos =  [(tipo.tipos,tipo.tipos)for tipo in DBTipos.query.all()]
    frmSalidas.tipo_ingreso.choices = tipos_ingresos
    lista_salidas = DBSalidas.query.order_by(DBSalidas.id_salida)
    if frmSalidas.validate_on_submit():
        desc = DBIngresos.query.filter(DBIngresos.descripcion == frmSalidas.descripcion.data,DBIngresos.tipo_ingreso == frmSalidas.tipo_ingreso.data).first()
        descuento_final = int(desc.cantidad) - (int(frmSalidas.cantidad.data))
        desc.cantidad=descuento_final
        db.session.add(desc)
        db.session.commit()
        nueva_salida = DBSalidas(frmSalidas.fecha.data,frmSalidas.solicita.data,frmSalidas.descripcion.data,frmSalidas.unidad.data,frmSalidas.tipo_ingreso.data,frmSalidas.cantidad.data,frmSalidas.observaciones.data)
        db.session.add(nueva_salida)
        db.session.commit()
        flash("Salida completada Exitosamente!")
        return redirect(url_for('salidas_bp.salidas_add'))
    if frmSalidas.errors:
        flash(frmSalidas.errors, "danger")
    return render_template("salidas.html",salidas = lista_salidas,form = frmSalidas)
@salidas_bp.route('/editar-salida/<int:id>',methods=['GET','POST'])
def salida_edit(id):
    id_salida = DBSalidas.query.get_or_404(id)
    form_edit_salida = FrmEditSalida(meta={'csrf': False})
    list_descripcion = [(des.descripcion,des.descripcion)for des in DBMateriales.query.all()]
    form_edit_salida.descripcion.choices = list_descripcion
    fecha = id_salida.fecha
    fecha_dt = datetime.strptime(fecha, '%Y-%m-%d')
    form_edit_salida.fecha.data = fecha_dt
    form_edit_salida.solicita.data = id_salida.solicita
    form_edit_salida.descripcion.data = id_salida.descripcion
    form_edit_salida.unidad.data = id_salida.unidad
    form_edit_salida.tipo_ingreso.data = id_salida.tipo_ingreso
    form_edit_salida.cantidad.data = id_salida.cantidad
    form_edit_salida.observaciones.data = id_salida.observaciones
    if form_edit_salida.validate_on_submit():
        nuevo_dato = DBSalidas.query.filter(DBSalidas.id_salida == id).first()
        nuevo_dato.fecha = request.form['fecha']
        nuevo_dato.solicita = request.form['solicita']
        nuevo_dato.descripcion = request.form['descripcion']
        nuevo_dato.unidad = request.form['unidad']
        nuevo_dato.tipo_ingreso = request.form['tipo_ingreso']
        nuevo_dato.cantidad = request.form['cantidad']
        nuevo_dato.observaciones = request.form['observaciones']
        db.session.add(nuevo_dato)
        db.session.commit()
        flash("Salida Editada Exitosamente!")
        return redirect(url_for('salidas_bp.salidas_add'))
    if form_edit_salida.errors:
        flash(form_edit_salida.errors, "danger")
    return render_template("editar_salida.html",form = form_edit_salida, id_salida=id_salida)
@salidas_bp.route('/eliminar-salida/<int:id>',methods=['GET','POST'])
def salida_del(id):
    del_salida = DBSalidas.query.filter(DBSalidas.id_salida == id).first()
    db.session.delete(del_salida)
    db.session.commit()
    flash("Salida eliminada Exitosamente!")
    return redirect(url_for('salidas_bp.salidas_add'))