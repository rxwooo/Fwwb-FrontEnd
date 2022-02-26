from application import db
from flask_login import UserMixin


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))
    
class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    imagename = db.Column(db.String(30))
    path = db.Column(db.String(100))

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    imageid = db.Column(db.Integer)
    classid = db.Column(db.Integer)
    score = db.Column(db.Integer)
    min_x = db.Column(db.Integer)
    max_x = db.Column(db.Integer)
    min_y = db.Column(db.Integer)
    max_y = db.Column(db.Integer)

class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    classname = db.Column(db.String(20))
    

    
