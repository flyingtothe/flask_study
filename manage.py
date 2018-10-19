# 使用 flask—script，需要使用 manage.py 文件

from flask_script import Manager
from app_11 import app
from app_11_db import DBmanager

manager = Manager(app)

@manager.command
def runserver():
    print('aaaa')

# 在 manage.py 中写指令 python manage.py commandname
# 将命令集中在一个文件中，需要使用 python manage.py db init
manager.add_command('db', DBmanager)

if __name__ == '__main__':
    manager.run()