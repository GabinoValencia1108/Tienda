from WebApp import db
class DBIngresos(db.Model):
    __tablename__="Ingresos"
    id_ingreso = db.Column(db.Integer,primary_key=True,autoincrement=True)
    fecha = db.Column(db.String(255))
    tipo_ingreso = db.Column(db.String(255))
    descripcion = db.Column(db.String(255))
    cantidad = db.Column(db.String(255))
    def __init__(self,fecha,tipo_ingreso,descripcion,cantidad):
        self.fecha = fecha
        self.tipo_ingreso = tipo_ingreso
        self.descripcion = descripcion
        self.cantidad = cantidad
    def __repr__(self) -> str:
        return "<DBIngresos %r>" % self.id_ingreso