
from datetime import datetime
from flask import render_template,Blueprint,request,send_file
from fpdf import FPDF
from ...model.frmInvsalida import FrmInvsalida
from ...model.DBSalidas import DBSalidas
from flask_login import login_required
from datetime import datetime
salidainv_bp = Blueprint("salidainv_bp",__name__)
@salidainv_bp.before_request
@login_required
def constructor():
    pass
@salidainv_bp.route('/salida/',methods=['GET','POST'])
def salidainv_add():
    frmInvsalida = FrmInvsalida(meta={'csrf': False})
    return render_template("invsalida.html",form = frmInvsalida)
@salidainv_bp.route('/download_salida/',methods=['GET','POST'])
def download_salida():
    f=request.form['fecha_inicio']
    f2=request.form['fecha_fin']
    fecha_actual = datetime.now()
    datos = DBSalidas.query.filter(DBSalidas.fecha>=f,DBSalidas.fecha<=f2).all()
    #Creación del pdf
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_author("Powered By Gabino García")
        pdf.set_font('Arial', 'B', 10)
        pdf.set_text_color(0 ,0,0)
        pdf.image("WebApp/static/img/images.png",20,10,30,18)
        pdf.cell(0, 15, 'COORDINACIÓN GENERAL DE MODERNIZACIÓN\n',0,1,"C")
        pdf.cell(0, 1, 'ADMINISTRATIVO E INNOVACIÓN GUBERNAMENTAL (CGMAIG)\n',0,1,"C")
        pdf.set_font('Arial', '', 11)
        pdf.multi_cell(0,10,"",0)
        pdf.multi_cell(35,10,"FECHA",1,"C")
        pdf.cell(10,6,"Día",1)
        pdf.cell(10,6,"Mes",1)
        pdf.cell(15,6,"Año",1,)
        pdf.set_font('Arial', 'B', 11)
        pdf.cell(120,6,"REGISTRO DE INVENTARIO SALIDA",0,1,"C")
        pdf.set_font('Arial', '', 10)
        pdf.cell(10,6,str(fecha_actual.day),1)
        pdf.cell(10,6,str(fecha_actual.month),1)
        pdf.cell(15,6,str(fecha_actual.year),1)
        pdf.multi_cell(120,9,"",0)

        ###tabla
        pdf.set_font('Arial', 'B', 9)
        pdf.cell(8,8,"No",1)
        pdf.cell(20,8,"FECHA",1)
        pdf.cell(40,8,"SOLICITA",1)
        pdf.cell(60,8,"DESCRIPCIÓN",1)
        pdf.cell(25,8,"TIPO SALIDA",1)
        pdf.multi_cell(0,8,"CANT.",1)
        #BODY
        #25 registros
        pdf.set_font('Arial', '', 7)
        c=0
        for i in datos:
            c+=1
            print(c)
            pdf.cell(8,6,str(c),1)
            pdf.cell(20,6,i.fecha,1)
            pdf.cell(40,6,i.solicita,1)
            pdf.cell(60,6,i.descripcion,1)
            pdf.cell(25,6,i.tipo_salida,1)
            pdf.multi_cell(0,6,i.cantidad,1)
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
        pdf.output('WebApp/static/'+f+f2+'.pdf','F')
        return send_file("static/"+f+f2+".pdf",None,as_attachment=True)
    except:
        pass
    return render_template("pdfsal.html",fecha=f)
    