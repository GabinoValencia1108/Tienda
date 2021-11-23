from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField,SelectField
from wtforms.validators import DataRequired, InputRequired
from WebApp import db
class StockTienda(db.Model):
    __tablename__='productos'
    id_producto = db.Column(db.BigInteger,primary_key=True,autoincrement=True)
    nombre_producto = db.Column(db.String(255))
    descripcion = db.Column(db.String(255))
    tipos = db.Column(db.String(255))
    categoria = db.Column(db.String(255))
    almacen = db.Column(db.String(255))
    cantidad = db.Column(db.String(255))
    def __init__(self,nombre_producto,descripcion,tipos,categoria,almacen,cantidad):
        self.nombre_producto = nombre_producto
        self.descripcion = descripcion
        self.tipos = tipos
        self.categoria = categoria
        self.almacen = almacen
        self.cantidad = cantidad
    def __repr__(self):
        return '<StockTienda %r>' % self.nombre_producto
class Nueva_SalidaTienda(db.Model):
    __tablename__='salidas'
    id_salida = db.Column(db.BigInteger,primary_key=True)
    codigo = db.Column(db.String(255))
    nombre_producto = db.Column(db.String(255))
    descripcion = db.Column(db.String(255))
    tipos = db.Column(db.String(255))
    no_de_documento = db.Column(db.Integer)
    nombre_empleado = db.Column(db.String(255))
    fecha_registro = db.Column(db.DateTime)
    cantidad = db.Column(db.String(255))
    def __init__(self,id_salida,codigo,nombre_producto,descripcion,tipos,no_de_documento,nombre_empleado,fecha_registro,cantidad):
        self.id_salida = id_salida
        self.codigo = codigo
        self.nombre_producto = nombre_producto
        self.descripcion = descripcion
        self.tipos = tipos
        self.no_de_documento = no_de_documento
        self.nombre_empleado = nombre_empleado
        self.fecha_registro = fecha_registro
        self.cantidad = cantidad
    def __repr__(self):
        return '<Nueva_SalidaTienda %r>' % self.id_salida
class Proveedores_Tienda(db.Model):
    __tablename__='Proveedores'
    id_proveedores = db.Column(db.BigInteger,primary_key=True)
    nombre_proveedor = db.Column(db.String(255))
    numero_pedido = db.Column(db.Integer)
    def __init__(self,id_proveedores,nombre_proveedor,numero_pedido):
        self.id_proveedores = id_proveedores
        self.nombre_proveedor = nombre_proveedor
        self.numero_pedido = numero_pedido
    def __repr__(self):
        return '<Proveedores_Tienda %r>' % self.id_proveedores
class ProductForm(FlaskForm):
    nombre_producto = SelectField("Seleccionar producto",coerce=str)
    descripcion = StringField("Descripcion:",validators=[InputRequired()])
    tipos = SelectField("Tipos:",validators=[InputRequired()],choices=[('Paquete', 'Paquete'), ('Pieza', 'Pieza'),('Rollo','Rollo'),('Litro','Litro'),('Metro','Metro'),('Caja','Caja'),('Kilogramo','Kilogramo'),('Garrafon','Garrafon'),('Galon','Galon')],coerce=str)
    categoria  = StringField("Categoria:",validators=[InputRequired()])
    proveedor = SelectField("Proveedor:",validators=[InputRequired()],choices=[('gobierno', 'gobierno'), ('donación', 'donación')],coerce=str)
    cantidad = StringField("Cantidad:",validators=[InputRequired()])
    #catalogo = SelectField("Catalogo:")
class NuevaSalidaForm(FlaskForm):
    id_salida = StringField("Id:",validators=[InputRequired()])
    codigo = StringField("Código:",validators=[InputRequired()])
    nombre_producto = StringField("Nombre del producto:",validators=[InputRequired()])
    descripcion = StringField("Descripcion:",validators=[InputRequired()])
    no_de_documento  = IntegerField("No de documento:",validators=[InputRequired()])
    nombre_empleado = StringField("Nombre del empleado:",validators=[InputRequired()])
    fecha_registro = DateField("Fecha de entrega:", validators=[DataRequired()], format='%d-%m-%Y')
    cantidad = StringField("Cantidad:",validators=[InputRequired()])
class ProveedorForm(FlaskForm):
    id_proveedores = IntegerField("Id Proveedor:",validators=[InputRequired()])
    nombre_proveedor = StringField("Nombre:",validators=[InputRequired()])
    numero_pedido = IntegerField("No de Pedido",validators=[InputRequired()])



