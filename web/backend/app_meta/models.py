from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class AppMeta(db.Model):
    id_num = db.Column(db.Integer)
    id_str = db.Column(db.String(128))
    name = db.Column(db.String(128))
    hl = db.Column(db.String(2), default='en')
    content = db.Column(db.String())

    def __init__(self, id_str, name, hl, content):
        self.id_str = id_str
        self.name = name
        self.hl = hl
        self.content = content
