from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func
    

class Accounts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    savings = db.Column(db.Integer)
    checkings = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone = True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(10))
    firstName = db.Column(db.String(10))
    lastName = db.Column(db.String(10))
    accounts = db.relationship('Accounts')
