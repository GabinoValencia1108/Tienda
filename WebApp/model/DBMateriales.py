from WebApp import db
class DBMateriales(db.Model):
    __tablename__="materiales"
    id_materiales = db.Column(db.Integer,primary_key=True,autoincrement=True)
    descripcion = db.Column(db.String(255))
    unidad = db.Column(db.String(255))
    categoria = db.Column(db.String(255))
    stock = db.Column(db.String(255))
    def __init__(self,descripcion,unidad,categoria,stock):
        self.descripcion = descripcion
        self.unidad = unidad
        self.categoria = categoria
        self.stock = stock
    def __repr__(self) -> str:
        return "<DBMateriales %r>" % self.id_materiales