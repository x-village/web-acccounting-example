from app import db


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=True)
    cost = db.Column(db.Integer, nullable=True)
