from flask_restplus import Api

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-Token'
    }
}

api = Api(version='1.0', title='OPS API', description='OPS API', authorizations=authorizations)
api.namespaces.pop(0)
ns = api.namespace('v1', description='这是自定义名称空间')
from .user import UserView
