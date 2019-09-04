from . import db
from .base import Base
from datetime import datetime

class Role(Base):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    users = db.relationship('User',backref='role',lazy='dynamic')
    create_time = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return '<Role %r>' % self.name