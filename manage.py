from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# from app_11 import app
# from app_11_db import DBmanager

# from app_13 import app
# from app_13_exts import db
# from app_13_models import Article

from app_object import app
from app_object_exts import db

manager = Manager(app)

# @manager.command
# def runserver():
#     print('aaaa')
# 在 manage.py 中写指令 python manage.py commandname
# 将命令集中在一个文件中，需要使用 python manage.py db init
# manager.add_command('db', DBmanager)

'''
命令：
初始化迁移环境：python manage.py db init
生成迁移映射文件：python manage.py db migrate
文件映射到表：python manage.py db upgrade
注意：需在 maanage.py 导入模型，否则不成功
'''
# flask_migrate 使用方法
# 1.绑定 app 和 db
migrate = Migrate(app, db)
# 2.将 MigrateCommand 命令添加到 manager 中
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()