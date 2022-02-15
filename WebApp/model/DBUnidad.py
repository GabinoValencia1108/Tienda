from WebApp import db
class DBUnidad(db.Model):
    __tablename__="unidad"
    id_unidad = db.Column(db.Integer,primary_key=True,autoincrement=True)
    unidad = db.Column(db.String(255))
    def __init__(self,unidad):
        self.unidad = unidad
    def __repr__(self):
        return "<DBUnidad %r>" % self.unidad