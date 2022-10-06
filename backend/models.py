from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String)

class Stacks(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    stack_name = db.Column(db.String(255),unique=True)
    last_cve = db.Column(db.String(255),unique=True)