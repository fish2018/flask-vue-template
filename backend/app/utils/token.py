from functools import wraps
from flask import request
from itsdangerous import SignatureExpired, BadSignature
from app.models import User
from flask import jsonify

def token_required(f):
    '''
    验证前端发来请求头中携带的token
    '''
    @wraps(f)
    def decorated(*args,**kwargs):
        token = None
        if 'X-Token' in request.headers:
            token = request.headers['X-Token']
        try:
            User.verify_auth_token(token)
        except SignatureExpired as e:
            return jsonify({"code":50014,"message": "token过期"}) # valid token, but expired
        except BadSignature as e:
            return jsonify({"code": 50008, "message": "无效token"})  # invalid token
        except Exception as e:
            return jsonify({"code": 50012, "message": "其他客户端登录"})
        return f(*args,**kwargs)
    return decorated
