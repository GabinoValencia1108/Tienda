from WebApp import db
class DBSalidas(db.Model):
    __tablename__="salidas"
    id_salida = db.Column(db.Integer,primary_key=True,autoincrement=True)
    fecha=db.Column(db.String(255))
    solicita =db.Column(db.String(255))
    descripcion =db.Column(db.String(255))
    tipo_salida = db.Column(db.String(255))
    cantidad=db.Column(db.String(255))
    observaciones=db.Column(db.String(255))
    def __init__(self,fecha,solicita,descripcion,tipo_salida,cantidad,observaciones): 
        self.fecha = fecha
        self.solicita = solicita
        self.descripcion = descripcion
        self.tipo_salida = tipo_salida
        self.cantidad = cantidad
        self.observaciones = observaciones 
        
        self.fecha = fecha
    def __repr__(self) -> str:
        return "<DBSalidas %r>" % self.descripcion