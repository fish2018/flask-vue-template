from flask_restplus import Resource,fields as filed
from app.api import ns
from app.models import User,Role
from app.marshalling import user_schema,users_schema,role_schema,gma
from flask import request,jsonify,current_app
from app.utils import token_required

# 给swagger用
class Model(object):
    post_model = ns.model('填写用户信息', {
        'username': filed.String,
        'password': filed.String,
        'role': filed.String
    })
    login_model = ns.model('登陆信息', {
        'username': filed.String,
        'password': filed.String
    })
    token_model = ns.model('Token',{
        'token': filed.String
    })


@ns.route('/user/createuser/',endpoint='createuser',methods=['POST'])
class CreateUserView(Resource):
    @ns.doc(body=Model.post_model, desciption='填写用户信息')
    def post(self):
        '''
        创建用户
        '''
        json_data = request.get_json()
        username = json_data['username']
        password = json_data['password']
        role = json_data['role']
        from app.models import db
        if Role.query.filter_by(name=role).first():
            role = Role.query.filter_by(name=role).first()
        else:
            role = Role(name=role)
        if not User.query.filter_by(username=username).first():
            user = User(username=username, password=password, role=role)
            db.session.add(user)
            db.session.commit()
        data = {
            "code": 20000,
            "data":None
        }
        return gma.dump(data)

@ns.route('/users/',endpoint='users',methods=['GET','OPSTIONS'])
class UserView(Resource):
    # @ns.doc(security='apikey')
    # decorators = [token_required] 方法一
    # method_decorators = [token_required] # 方法二
    # @token_required 方法三
    def get(self):
        '''
        获取用户列表
        '''
        users = User.query.all()
        result = users_schema.dump(users)
        data = {
            'code': 20000,
            'data': result
        }
        current_app.logger.info('获取用户列表')
        return gma.dump(data)

@ns.route('/user/<int:id>',endpoint='user',doc=False)
class UserView(Resource):
    def get(self,id):
        '''
        获取用户名、密码
        '''
        user = User.query.filter_by(id=id).first()
        result = user_schema.dump(user)
        data = {
            "code":20000,
            "data":result
        }
        return gma.dump(data)

@ns.route('/role/<int:id>',endpoint='role',doc=False)
class RoleView(Resource):
    def get(self,id):
        '''
        根据用户id获取角色
        '''
        role = Role.query.filter_by(id=id).first()
        result = role_schema.dump(role)
        data = {
            "code":20000,
            "data":result
        }
        return gma.dump(data)

@ns.route('/user/login',endpoint='login',methods=['POST'])
class LoginView(Resource):
    @ns.doc(body=Model.login_model, desciption='登录信息')
    def post(self):
        '''
        用户登录，获取token
        '''
        json_data = request.get_json()
        username = json_data['username']
        password = json_data['password']
        user = User.query.filter_by(username=username).first()
        if user.verify_password(password):
            token = user.generate_auth_token()
        else:
            return '验证失败'
        data = {
            'code':20000,
            'data':{
                "token":token.decode('ascii')
            }
        }
        current_app.logger.info('登录用户')
        return gma.dump(data)


@ns.route('/user/info',endpoint='getinfo',methods=['GET'])
class UserInfo(Resource):
    @ns.doc(params={'token': '根据token获取用户信息'})
    # @token_required
    def get(self,*args,**kwargs):
        '''
        根据token获取用户信息
        '''
        token = request.args.get('token')
        try:
            user = User.verify_auth_token(token)
        except Exception as e:
            return jsonify({"code": 50012, "message": "token过期"})

        data = {
            'code': 20000,
            "data":{
                'token':token,
                'roles':user.role.name,
                'name':user.username,
                'avatar': None
            }
        }
        current_app.logger.info('获取用户信息')
        return gma.dump(data)


@ns.route('/user/logout',endpoint='logout',methods=['POST'])
class LogoutView(Resource):
    @ns.doc(body=Model.token_model, desciption='token')
    def post(self):
        '''
        用户登出
        '''
        data = {
            'code' : 20000,
            "data":{'token':None,"message": "用户登出"}
        }
        return gma.dump(data)
