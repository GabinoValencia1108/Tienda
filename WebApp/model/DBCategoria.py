from WebApp import db
class DBCategoria(db.Model):
    __tablename__="categoria"
    id_categoria = db.Column(db.Integer,primary_key=True,autoincrement=True)
    categoria = db.Column(db.String(255))
    def __init__(self,categoria):
        self.categoria = categoria
    def __repr__(self):
        return "<DBCategoria %r>" % self.categoria 