from . import ma
from app.models import Role
# 序列化角色表
class RoleSchema(ma.ModelSchema):
    class Meta:
        # fields = ('name',)
        model = Role

role_schema = RoleSchema()
roles_schema = RoleSchema(many=True)


