from WebApp import db
class DBTipos(db.Model):
    __tablename__="tipos"
    id_tipos = db.Column(db.Integer,primary_key=True,autoincrement=True)
    tipos = db.Column(db.String(255))
    def __init__(self,tipos):
        self.tipos = tipos
    def __repr__(self) -> str:
        return "<DBTipos %r>" % self.tipos