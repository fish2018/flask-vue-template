from app.models import db
from app import create_app
from app.models.base import Base
from app.models.role import Role
from app.models.user import User
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand


'''
python3 manage.py db init
python3 manage.py db migrate -m "initial migration"
python3 manage.py db upgrade
'''


app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
