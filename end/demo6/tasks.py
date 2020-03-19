"""pip install celery安装 celery
安装Redis数据库
pip install redis 安装python 处理redis数据库驱动
"""

from celery import Celery
import time

# celery 操作由celery实例开始
# app = Celery("tasks", broker="redis://127.0.0.1:6379/0")

# 构建任务
# @app.task()
# def dosomething():
#     "耗时任务"
#     print("开始执行")
#     time.sleep(5)
#     print("执行结束")


from flask_mail import Message
from views import mail
from factory import create_app
app = Celery("tasks", broker="redis://localhost:6379/1")

@app.task
def sendmail(email,serstr):
    with create_app().app_context():
        msg = Message(subject="账号注册激活邮件", recipients=[email])
        msg.body = "testing"
        msg.html = "<a href='http://127.0.0.1:5000/active/%s'>点击激活</a>" % (serstr,)
        mail.send(msg)
        # print("发送成功！")

# @app.task()
# def sendmail(email,serstr):
#     # with.current_app().app_context():
#     msg = Message(subject="账号注册激活邮件", recipients=[email])
#     msg.body = "testing"
#     msg.html = "<a href='http://127.0.0.1:5000/active/%s'>点击激活</a>" % (serstr,)
#     mail.send(msg)