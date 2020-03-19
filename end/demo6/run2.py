# from  factory import  create_app
# from views import  *
#
# if __name__ == '__main__':
#     create_app().run(host="127.0.0.1", port=5000, debug=True)
#

from flask import Flask,request,Blueprint,render_template,flash

app = Flask(__name__)

carbp = Blueprint("car", __name__)
# @carbp.route("/")
# def index():
#     carlist = [
#         {"id": 101, "name": "玛莎拉蒂"},
#         {"id": 102, "name": "法拉利"},
#         {"id": 103, "name": "奥迪"}
#                ]
#     return render_template("index.html", carlist=carlist, username="rhy")
#
# @app.template_filter()
# def myupperfun(value):
#     return value.capitalize()

userbp = Blueprint("user", __name__)
# @userbp.route("/login/",methods=["GET","POST"])
# def login():
#     if request.method == "GET":
#         return render_template("login.html")
#         # return "<h1>这里是登录界面<h1>"
#     elif request.method == "POST":
#         error= None
#         username = request.form.get("username")
#         password = request.form.get("password")
#         #return "<h1>这里是提取登录数据界面<h1><br>
#         #t1 = (username, password)
#         if username == "":
#             error = "用户名不能为空！"
#         elif password == "":
#             error = "密码不能为空！"
#
#         if error:
#             flash(error)
#             return render_template("login.html")
#         else:
#             return "%s---%s"%(username,password)
#
# @userbp.route('/register/', methods=["GET", "POST"])
# def register():
#     if request.method == "GET":
#         return render_template("register.html")
#     elif request.method == "POST":
#         error = None
#         username = request.form.get("username")
#         password = request.form.get("password")
#         password1 = request.form.get("password1")
#
#         if not username:
#             error = "用户名不能为空！"
#         elif not password:
#             error = "密码不能为空！"
#         elif password != password1:
#             error = "两次输入密码不相同！"
#
#         if error:
#             flash(error)
#             return render_template("register.html")
#         else:
#             return "%s---%s" % (username, password)


#将蓝图注册到应用
app.register_blueprint(carbp)
app.register_blueprint(userbp)

if __name__ == '__main__':
    app.run(debug=True)
