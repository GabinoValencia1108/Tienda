from WebApp import db
class DBSalidas(db.Model):
    __tablename__="salidas"
    id_salida = db.Column(db.Integer,primary_key=True,autoincrement=True)
    fecha=db.Column(db.String(255))
    solicita =db.Column(db.String(255))
    descripcion =db.Column(db.String(255))
<<<<<<< HEAD
    tipo_salida = db.Column(db.String(255))
    cantidad=db.Column(db.String(255))
    observaciones=db.Column(db.String(255))
    def __init__(self,fecha,solicita,descripcion,tipo_salida,cantidad,observaciones): 
        self.fecha = fecha
        self.solicita = solicita
        self.descripcion = descripcion
        self.tipo_salida = tipo_salida
=======
    unidad =db.Column(db.String(255))
    tipo_ingreso = db.Column(db.String(255))
    cantidad=db.Column(db.String(255))
    observaciones=db.Column(db.String(255))
    def __init__(self,fecha,solicita,descripcion,unidad,tipo_ingreso,cantidad,observaciones): 
        self.fecha = fecha
        self.solicita = solicita
        self.descripcion = descripcion
        self.unidad = unidad
        self.tipo_ingreso = tipo_ingreso
>>>>>>> 0c2907a5d5b52b79ad110ed80370c7436a46e41d
        self.cantidad = cantidad
        self.observaciones = observaciones 
        
        self.fecha = fecha
    def __repr__(self) -> str:
        return "<DBSalidas %r>" % self.descripcion