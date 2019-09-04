# flask-vue-template
基于flask和vue的前后端整合框架，开箱即用
后端使用flask-restplus开发，自带swagger，基于flask_marshmallow序列化对象，orm使用flask-sqlalchemy，已经集成基于token的用户认证，日志功能

# 后端backend

使用方法：

修改app/config/settings.py指定开发环境配置文件
```
APP_ENV = DevelopmentConfig
```

根据自己情况修改app/config/dev.py配置数据库信息，数据库提前创建
```
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/PMS?charset=utf8mb4'
```

初始化数据库
```
python3 manage.py db init
python3 manage.py db migrate -m "initial migration"
python3 manage.py db upgrade
```

默认监听地址：host='0.0.0.0', port='5000' ，可以在app.py中修改

![](https://github.com/fish2018/flask-vue-template/blob/master/img/backend.jpg)

在swagger页面创建用户admin/admin

# 前端frontend

使用方法：

修改开发环境配置文件config/dev.env.js ，根据自己情况配置后端API地址，默认本机5000端口
```
BASE_API: '"http://127.0.0.1:5000/v1"'
```

启动
```
npm i
npm run dev
```

默认 http://0.0.0.0:9005 ，在config/index.js中修改
```
    host: '0.0.0.0',
    port: 9005,
```
