from flask_script import Manager

DBmanager = Manager()
# 子命令
@DBmanager.command
def init():
    print('初始化')

@DBmanager.command
def migrate():
    print('表迁移成功')