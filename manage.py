# 使用 flask—script，需要使用 manage.py 文件

from flask_script import Manager
from flask-study import app14

manager = Manager(app14)

@manager.command
def runserver():
    print('aaaa')

if __name__ == '__main__':
    manager.run()