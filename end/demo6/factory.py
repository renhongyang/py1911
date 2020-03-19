"""
flask 应用工厂
"""
from flask import Flask,request,render_template,flash,url_for
from views import *
from models import *

def create_app():
    app = Flask(__name__)
    app.register_blueprint(carbp)
    app.register_blueprint(userbp)
    app.register_blueprint(adminbp)

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html')

    @app.template_filter()
    def myupperfun(value):
        return value.capitalize()

    # @app.before_first_request
    # def first_request_do_something():
    #     import sqlite3
    #     try:
    #         con = sqlite3.connect("demo6.db")
    #         cur = con.cursor()
    #         cur.execute("DROP TABLE IF EXISTS user;")
    #         cur.execute("CREATE TABLE user (  id INTEGER PRIMARY KEY AUTOINCREMENT,  "
    #                     "username TEXT UNIQUE NOT NULL,  password TEXT NOT NULL, "
    #                     "create_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, "
    #                     "is_admin INTEGER DEFAULT 0, is_active INTEGER DEFAULT 1 )")
    #         con.commit()
    #         cur.close()
    #         con.close()
    #     except Exception as error:
    #         print(error)
    #扩展工厂
    app.secret_key = "\xc4\xdb\xcc\x01h\xe0t|\x81\x05\xb6m\xb4P\xa8\xc4S\xba\xff\x89\xf7Q\x7f\xa8"
    app.config["MAIL_SERVER"] = "smtp.163.com"
    app.config["MAIL_PORT"] = 25
    # 可以选使用哪种协议
    # app.config["MAIL_USE_TLS"] = False
    # app.config["MAIL_USE_SSL"] = False
    app.config["MAIL_USERNAME"] = "qtdiq69834@163.com"
    app.config["MAIL_PASSWORD"] = "TBKHQPCDKMBRXLEV"
    app.config['MAIL_DEFAULT_SENDER'] = '注册账号激活<qtdiq69834@163.com>'
    mail.init_app(app)

    # 配置数据库(本地数据库)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///demo6.db'
    # 自动检测更新 关闭
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    db.app = app
    return app

