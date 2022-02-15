from datetime import datetime
from flask import Flask,render_template,Blueprint,flash,redirect,url_for,request,send_file
from fpdf import FPDF
from ...model.frmRequerimiento import FrmRequerimiento
from ...model.DBIngresos import DBIngresos
<<<<<<< HEAD
from flask_login import login_required
=======

>>>>>>> 0c2907a5d5b52b79ad110ed80370c7436a46e41d
from datetime import datetime
from ...model.DBMateriales import DBMateriales
from ...model.DBSalidas import DBSalidas
from WebApp import db
requerimiento_bp = Blueprint("requerimiento_bp",__name__)
<<<<<<< HEAD
@requerimiento_bp.before_request
@login_required
def constructor():
    pass
=======
>>>>>>> 0c2907a5d5b52b79ad110ed80370c7436a46e41d
@requerimiento_bp.route('/requerimiento/',methods=['GET','POST'])
def requerimiento_add():
    frmRequerimiento = FrmRequerimiento(meta={'csrf': False})
    return render_template("requerimiento.html",form = frmRequerimiento)
@requerimiento_bp.route('/download/',methods=['GET','POST'])
def download():
    f= request.form['fecha_inicio']
    f2= request.form['fecha_fin']
    fecha_actual = datetime.now()
    datos = DBIngresos.query.filter(DBIngresos.fecha>=f,DBIngresos.fecha <=f2).all()
    #creacion pdf
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_author("Powered By Daniel Marín")
        pdf.set_font('Arial', 'B', 10)
        pdf.set_text_color(0 ,0,0)
        pdf.image("images.png",20,10,25,15)
        pdf.cell(0, 5, 'SUBSECRETARÍA DE RECURSOS MATERIALES\n',0,1,"C")
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(0, 5, 'DIRECCIÓN DE CONTROL DE RECURSOS MATERIALES\n',0,1,"C")
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(0, 5, 'ALMACEN GENERAL\n',0,1,"C")
        pdf.set_font('Arial', '', 11)
        pdf.multi_cell(0,10,"",0)
        pdf.multi_cell(35,10,"Fecha",1,"C")
        pdf.cell(10,6,"Dia",1)
        pdf.cell(10,6,"Mes",1)
        pdf.cell(15,6,"Año",1)
        pdf.set_font('Arial', 'B', 11)
        pdf.cell(120,6,"REQUERIMIENTO DE MATERIAL",0,0,"C")
        pdf.multi_cell(0,6,"Folio",1,"C")
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(10,6,"30",1)
        pdf.cell(10,6,"11",1)
        pdf.cell(15,6,"2021",1)
        pdf.cell(35,10,"",0)
        pdf.cell(50,6,"PARTIDA: 21101",1)
        pdf.cell(35,10,"",0)
        pdf.multi_cell(0,6,"#Folio",1,"C")
        pdf.multi_cell(0,4,"",0)
        pdf.set_fill_color(130, 129, 129)
        pdf.cell(0,5,"UNIDAD ADMINISTRATIVA SOLICITANTE",1,1,"C",1)
        pdf.set_font('Arial', '', 10)
        pdf.cell(0,8,"COORDINACIÓN DE MODERNIZACIÓN ADMINISTRATIVA E INNOVACIÓN GUBERNAMENTAL",1,1,"C")
        pdf.set_font('Arial', 'B', 10)
        pdf.set_fill_color(130, 129, 129)
        pdf.cell(0,5,"AREA ASIGNADA",1,1,"C",1)
        pdf.set_font('Arial', '', 10)
        pdf.cell(0,8,"SUPERVISIÓN DE CALIDAD Y EVALUACIÓN",1,1,"C",0)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(20,8,"LOTE",1, align='C', fill=1)
        pdf.cell(20,8,"CANTIDAD",1, align='C', fill=1)
        pdf.cell(20,8,"UNIDAD",1, align='C', fill=1)
        pdf.multi_cell(0,8,"DESCRIPCIÓN DEL MATERIAL",1, 'C', fill=1)
        #BODY
        #25 registros
        for i in range(25):
            pdf.cell(20,6,"#",1)
            pdf.cell(20,6,"#",1)
            pdf.cell(20,6,"#",1)
            pdf.multi_cell(0,6,"#",1)
        #ENDBODY
        pdf.rect(10,61.1,190.0,184,"D")
        pdf.set_xy(10,250)
        pdf.cell(48,5,"AUTORIZÓ",0,0,"C")
        pdf.cell(65,5,"",0)
        pdf.multi_cell(0,5,"SOLICITÓ",0,"C")
        pdf.multi_cell(0,3,"",0,"C")
        pdf.multi_cell(0,3,"",0,"C")
        pdf.set_font('Arial', 'B', 11)
        pdf.cell(57,5,"SILVIA ELENA FLORES BANDA",0,0,"C")
        pdf.set_font('Arial', '', 11)
        pdf.cell(55,5,"",0)
        pdf.set_font('Arial', 'B', 11)
        pdf.multi_cell(0,5,"TERESA DE JESUS LOPEZ HERNANDEZ",0,0,"C")
        pdf.set_font('Arial', '', 11)
        pdf.cell(64,5,"SUBDIRECTORA DE SUPERVISIÓN",0,0,"C")
        pdf.cell(69,5,"",0)
        pdf.multi_cell(0,5,"ADMINISTRADOR",0,0,"C")
        pdf.cell(52,5,"DE CALIDAD Y EVALUACIÓN",0,0,"C")
        pdf.output('WebApp/static/'+f+'.pdf', 'F')
        return send_file("static/"+f+".pdf",None,as_attachment=True)
    except:
        pass
    return render_template("pdf.html",fecha=f)
# Powered By Gabino García

