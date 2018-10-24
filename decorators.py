from flask import redirect, url_for, session
from functools import wraps

# 登陆限制装饰器
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('user_id'):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login5'))
    return wrapper