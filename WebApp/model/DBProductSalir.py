from WebApp import db
class DBProductSalir(db.Model):
    __tablename__="salidas"
    id_salir = db.Column(db.Integer,primary_key=True,autoincrement=True)
    descripcion =db.Column(db.String(255))
    cantidad=db.Column(db.String(255))
    def __init__(self,descripcion,cantidad): 
        self.descripcion = descripcion
        self.cantidad = cantidad
    def __repr__(self) -> str:
        return "<DBProductSalir %r>" % self.descripcion