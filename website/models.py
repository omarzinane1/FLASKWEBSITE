from flask import app
from sqlalchemy import ForeignKey
from . import db
from flask_login import UserMixin 
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000)) 
    date = db.Column(db.DateTime(timezone=True), default = func.now())
     # Clé étrangère vers User.id
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150),unique =True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
     # Relation avec la table Note
    notes = db.relationship('Note', backref='User', lazy=True)
