from flask_script import Manager

DBmanager = Manager()
# 将子命令集中管理
@DBmanager.command
def init():
    print('初始化')

@DBmanager.command
def migrate():
    print('表迁移成功')