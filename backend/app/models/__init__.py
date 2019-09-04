from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .role import Role
