from flask import Flask,render_template,Blueprint,flash,redirect,url_for,request
from sqlalchemy.orm import query
from fpdf import FPDF
from ...model.frmInventario import FrmInventario

from datetime import datetime
from ...model.DBProductos import DBProductos
from ...model.DBSalidas import DBSalidas
from WebApp import db
inventario_bp = Blueprint("inventario_bp",__name__)
@inventario_bp.route('/inventario/',methods=['GET','POST'])
def inventario_add():
    frmInventario = FrmInventario(meta={'csrf': False})
    consulta = DBSalidas.query.all()
    
    pdf = FPDF(orientation = 'P', unit= 'mm', format='A4')
    pdf.add_page()
#logo
    #pdf.image('logo.png', x=20, y=10, w=30, h=18,)
    pdf.set_left_margin(20)
    pdf.set_right_margin(20)
    #titulo
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(w = 0, h=5, txt='(CGMAIG) COORDINACIÓN GENERAL DE MODERNIZACIÓN', border=0, align='C', fill=0, ln=1,) 
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(w = 0, h=5, txt='ADMINISTRATIVO E INNOVACIÓN GUBERNAMENTAL', border=0, align='C', fill=0, ln=1,)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(w = 0, h=25, txt='REGISTRO DE INVENTARIO', border=0, align='C', fill=0, ln=40,)

#fecha
    pdf.set_font('Arial', 'B', 7)
    pdf.cell(w = 10, h = 10, txt = 'No', border = 1, align = 'C', fill = 0)
    pdf.cell(w = 22, h = 10, txt = 'FECHA', border = 1, align = 'C', fill = 0)
    pdf.cell(w = 60, h = 10, txt = 'DESCRIPCIÓN', border = 1, align = 'C', fill = 0)
    pdf.cell(w = 25, h = 10, txt = 'UNIDAD', border = 1, align = 'C', fill = 0)
    pdf.cell(w = 25, h = 10, txt = 'CATEGORÍA', border = 1, align = 'C', fill = 0)
    pdf.cell(w = 16, h = 10, txt = 'SALIDA', border = 1, align = 'C', fill = 0)
    pdf.multi_cell(w = 0, h = 10, txt = 'STOCK', border = 1, align = 'C', fill = 0)

##ejemplo de datos
    x=0
    for i in consulta:
        x=x+1
        pdf.cell(w = 10, h = 5, txt = str(x), border = 1, align = 'C', fill = 0)
        pdf.cell(w = 22, h = 5, txt = str(x), border = 1, align = 'C', fill = 0)
        pdf.cell(w = 60, h = 5, txt = "c", border = 1, align = 'C', fill = 0)
        pdf.cell(w = 25, h = 5, txt = "i", border = 1, align = 'C', fill = 0)
        pdf.cell(w = 25, h = 5, txt = "i", border = 1, align = 'C', fill = 0)
        pdf.cell(w = 16, h = 5, txt = "i", border = 1, align = 'C', fill = 0)
        #pdf.multi_cell(w = 0, h = 5, txt = valor[6], border = 1, align = 'C', fill = 0)

    pdf.output('Inventario.pdf')
    if frmInventario.validate_on_submit():
        pass
    if frmInventario.errors:
        
        flash(frmInventario.errors, "danger")
    return render_template("inventario.html",form = frmInventario)