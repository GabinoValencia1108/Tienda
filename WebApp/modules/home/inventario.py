from re import L
from flask import Flask,render_template,Blueprint,flash,redirect,url_for,request,send_file
from fpdf import FPDF
from ...model.frmInventario import FrmInventario
from ...model.DBIngresos import DBIngresos

from datetime import datetime
from ...model.DBStock import DBStock
from ...model.DBSalidas import DBSalidas
from WebApp import db
inventario_bp = Blueprint("inventario_bp",__name__)
@inventario_bp.route('/inventario/',methods=['GET','POST'])
def inventario_add():
    frmInventario = FrmInventario(meta={'csrf': False})
    return render_template("inventario.html",form = frmInventario)
@inventario_bp.route('/download/',methods=['GET','POST'])
def download():
    f= request.form['fecha_inicio']
    datos = DBIngresos.query.filter(DBIngresos.fecha == f).all()
    datos_salida = DBSalidas.query.order_by(DBSalidas.cantidad).all()
    #creacion pdf
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_author("Powered By Gabino García")
        pdf.set_font('Arial', 'B', 10)
        pdf.set_text_color(0 ,0,0)
        pdf.image("WebApp/static/img/logo2.png",20,10,30,18)
        pdf.cell(0, 5, '(CGMAIG) COORDINACIÓN GENERAL DE MODERNIZACIÓN\n',0,1,"C")
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(0, 5, 'ADMINISTRATIVO E INNOVACIÓN GUBERNAMENTAL\n',0,1,"C")
        pdf.set_font('Arial', '', 11)
        pdf.multi_cell(0,10,"",0)
        pdf.multi_cell(35,10,"Fecha",1,"C")
        pdf.cell(10,6,"Dia",1)
        pdf.cell(10,6,"Mes",1)
        pdf.cell(15,6,"Año",1,)
        pdf.set_font('Arial', 'B', 11)
        pdf.cell(120,6,"REGISTRO DE INVENTARIO\n",0,1,"C")
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(10,6,"#",1)
        pdf.cell(10,6,"#",1)
        pdf.cell(15,6,"#",1,1)
        pdf.multi_cell(35,9,"",0)

        ####tabla
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(10,8,"No",1)
        pdf.cell(30,8,"FECHA",1)
        pdf.cell(70,8,"DESCRIPCIÓN",1)
        pdf.cell(30,8,"UNIDAD",1)
        pdf.cell(30,8,"CATEGORÍA",1)
        pdf.multi_cell(0,8,"STOCK",1)
        #BODY
        #25 registros
        pdf.set_font('Arial', '', 7)
        for i in datos:
            pdf.cell(10,6,"",1)
            pdf.cell(30,6,i.fecha,1)
            pdf.cell(70,6,i.descripcion,1)
            pdf.cell(30,6,i.unidad,1)
            pdf.cell(30,6,i.categoria,1)
            pdf.multi_cell(0,6,"#",1)
        #ENDBODY
        pdf.rect(10,61.1,190.0,184,"D")
        pdf.set_xy(10,250)
        pdf.multi_cell(0,5,"SOLICITÓ",0,"C")
        pdf.multi_cell(0,3,"",0,"C")
        pdf.multi_cell(0,3,"",0,"C")
        pdf.set_font('Arial', 'B', 11)
        pdf.multi_cell(0,5,"TERESA DE JESUS LOPEZ HERNANDEZ",0,"C")
        pdf.set_font('Arial', '', 11)
        pdf.multi_cell(0,5,"ADMINISTRADOR",0,"C")
        pdf.output('WebApp/static/'+f+'.pdf', 'F')
        return send_file("static/"+f+".pdf",None,as_attachment=True)
    except:
        pass
    return render_template("pdf.html",fecha=f)