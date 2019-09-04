from flask_marshmallow import Marshmallow
ma = Marshmallow()
from .general import gma
from .role import role_schema,roles_schema
from .user import user_schema,users_schema
