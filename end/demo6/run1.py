"""
    一个最小的 Flask 应用如下:
"""

from flask import Flask,request,render_template,flash,url_for
app = Flask(__name__)

app.secret_key ="\xc4\xdb\xcc\x01h\xe0t|\x81\x05\xb6m\xb4P\xa8\xc4S\xba\xff\x89\xf7Q\x7f\xa8"

@app.route('/',methods=["GET","POST"])
def index():
    carlist = [
        {"id": 101, "name": "玛莎拉蒂"},
        {"id": 102, "name": "法拉利"},
        {"id": 103, "name": "奥迪"}
               ]
    return render_template("index.html", carlist=carlist, username="rhy")

@app.template_filter()
def myupperfun(value):
    return value.capitalize()

@app.route('/login/',methods=["GET","POST"])
def login():
    #print(request,request.method,dir(request))
    if request.method == "GET":
        return render_template("login.html")
        # return "<h1>这里是登录界面<h1>"
    elif request.method == "POST":
        error= None
        username = request.form.get("username")
        password = request.form.get("password")
        #return "<h1>这里是提取登录数据界面<h1><br>
        #t1 = (username, password)
        if username == "":
            error = "用户名不能为空！"
        elif password == "":
            error = "密码不能为空！"

        if error:
            flash(error)
            return render_template("login.html")
        else:
            return "%s---%s"%(username,password)

@app.route('/register/',methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        error= None
        username = request.form.get("username")
        password = request.form.get("password")
        password1 = request.form.get("password1")

        if not username:
            error = "用户名不能为空！"
        elif not password:
            error = "密码不能为空！"
        elif password != password1:
            error = "两次输入密码不相同！"

        if error:
            flash(error)
            return render_template("register.html")
        else:
            return "%s---%s" % (username, password)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')



#启动web服务
if __name__ == '__main__':
    app.run(debug=True)
