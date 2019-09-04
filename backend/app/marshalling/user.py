from . import ma
from app.models import User
from flask_marshmallow import base_fields

# 序列化用户信息
class UserInfoSchema(ma.Schema):
    code = base_fields.Integer()
    data = ma.Dict()
user_info_schema = UserInfoSchema()

# 序列化用户表
class UserSchema(ma.ModelSchema):
    class Meta:
        # fields = ('username','password')
        model = User
    role = ma.HyperlinkRelated('role')
user_schema = UserSchema()
users_schema = UserSchema(many=True)