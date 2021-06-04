from app import db


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    has_rings = db.Column(db.Boolean)
