from app.ext.db import db
import sqlalchemy as col


class Url(db.Model):
    __tablename__ = 'urls'
    id = col.Column(col.Integer, primary_key=True, autoincrement=True)
    url_origem = col.Column(col.String(50))
    url_destino = col.Column(col.String(500))

    def __init__(self, url_destino, url_origem):
        self.url_destino = url_destino
        self.url_origem = url_origem
