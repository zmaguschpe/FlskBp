from . import db
from sqlalchemy.sql import func
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(22), unique=True)
    time_reg = db.Column(db.DateTime(timezone=True), default=func.now())
    password = db.Column(db.String(999))
    
    first_name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)

class Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(999))
    time = db.Column(db.DateTime(timezone=True), default=func.now())
    date = db.Column(db.Date(), default=func.current_date())

