from WebApp import db
class DBTipos(db.Model):
    __tablename__="tipos"
    id_tipos = db.Column(db.Integer,primary_key=True,autoincrement=True)
    tipos = db.Column(db.String(255))
    tipos_salida = db.Column(db.String(255))
    def __init__(self,tipos,tipos_salida):
        self.tipos = tipos
        self.tipos_salida = tipos_salida
    def __repr__(self) -> str:
        return "<DBTipos %r>" % self.tipos