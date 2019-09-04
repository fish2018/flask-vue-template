from . import ma
from flask_marshmallow import base_fields
# 通用序列化{"code":xxx,"data":xxx}
class GeneralSchema(ma.Schema):
    code = base_fields.Integer()
    data = ma.Dict()

gma = GeneralSchema()