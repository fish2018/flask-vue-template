from . import db
from datetime import datetime

class Base(db.Model):
    __abstract__ = True
    # id = db.Column(db.Integer, primary_key=True)
    # create_time = db.Column(db.DateTime,default=datetime.now)
