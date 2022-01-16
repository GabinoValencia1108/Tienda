from WebApp import db
class DBMateriales(db.Model):
    __tablename__="materiales"
    id_materiales = db.Column(db.Integer,primary_key=True,autoincrement=True)
    descripcion = db.Column(db.String(255))
    def __init__(self,descripcion):
        self.descripcion = descripcion
    def __repr__(self) -> str:
        return "<DBMateriales %r>" % self.descripcion