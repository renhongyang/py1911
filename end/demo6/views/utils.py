"""
视图工具模块
"""
# 扩展模块
from flask_mail import Mail
from flask import session,redirect,request
from functools import wraps

mail = Mail()

# 定义装饰器,检查登录状态
def checklogin(f):
    @wraps(f)
    def check(*args, **kwargs):
        # 可变列表参数，关键字参数
        username = session.get("username")
        if username:
            return f(*args, **kwargs)
        else:
            return redirect("/login/?next=+request.path")
    return check


