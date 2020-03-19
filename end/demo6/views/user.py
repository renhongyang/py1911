from flask import Blueprint,render_template,request,flash,redirect,current_app,session,make_response
import sqlite3
from werkzeug.security import generate_password_hash,check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer,BadSignature,SignatureExpired
from datetime import datetime ,timedelta

userbp = Blueprint("userbp",__name__)
@userbp.route("/login/", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
        # return "<h1>这里是登录界面<h1>"
    elif request.method == "POST":
        error = None
        email = request.form.get("email")
        password = request.form.get("password")
        #return "<h1>这里是提取登录数据界面<h1><br>
        #t1 = (username, password)
        if email == "":
            error = "邮箱不能为空！"
        elif password == "":
            error = "密码不能为空！"

        if error:
            flash(error)
            return render_template("login.html")
        else:
            with sqlite3.connect("demo6.db")as con:
                cur = con.cursor()
                cur.execute("select * from user where email = ?", (email,))
                r = cur.fetchall()
                print(r[0], "+++", r[0][2], password)
                if r[0][1] != email:
                    flash("邮箱不存在！")
                    return redirect("/login/")
                elif not check_password_hash(r[0][2], password):
                    flash("密码输入有误！")
                    return redirect("/login/")
                else:
                    if r[0][5] == 0:
                        flash("邮箱未激活,不能登录！")
                        return redirect("/login/")
                    else:
                        next = request.args.get("next")
                        if next:
                            res = make_response(redirect(next))
                            # res.set_cookie(key="username", value=email, expires=datetime.now()+timedelta(days=7))
                            session["username"] = email
                            return res
                        else:
                            res = make_response(redirect("/"))
                            # res.set_cookie(key="username", value=email, expires=datetime.now() + timedelta(days=7))
                            session["username"] = email
                            # return "%s---%s" % (email, password)
                            return res

@userbp.route("/loginout/")
def loginout():
    res = make_response(redirect("/"))
    # res.delete_cookie("username")
    session.pop("username")
    return res

@userbp.route('/register/', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        error = None
        email = request.form.get("email")
        password = request.form.get("password")
        password1 = request.form.get("password1")

        if not email:
            error = "邮箱不能为空！"
        elif not password:
            error = "密码不能为空！"
        elif password != password1:
            error = "两次输入密码不相同！"

        if error:
            flash(error)
            # return render_template("register.html")
            return redirect("/register/")
        else:
            with sqlite3.connect("demo6.db")as con:
                cur = con.cursor()
                cur.execute("select * from user where email = ?", (email,))
                r = cur.fetchall()
                # print(r, "+++")
                if len(r) > 0:
                    flash("邮箱已存在！")
                    return redirect("/register/")
                else:
                      try:
                            from flask_mail import Message
                            from .utils import mail
                            from tasks import sendmail
                            hashpassword = generate_password_hash(password1)
                            cur.execute("insert into user (email,password) values (?,?)", (email, hashpassword))

                            cur.execute("select id from user where email = ?", (email,))
                            userid = cur.fetchone()[0]
                            # print(userid)
                            serUtil = TimedJSONWebSignatureSerializer(current_app.secret_key, expires_in=3000)
                            serstr = serUtil.dumps({"userid": userid}).decode("utf-8")
                            sendmail(email, serstr)

                            # msg = Message(subject="账号注册激活邮件", recipients=[email])
                            # msg.body = "testing"
                            # msg.html = "<a href='http://127.0.0.1:5000/active/%s'>点击激活</a>" % (serstr,)
                            # mail.send(msg)
                            con.commit()
                            # return "%s---%s" % (email, password)
                            return "请去邮箱激活账号 %s" %(email)
                      except Exception as error:
                        print(error)
                        con.rollback()
                        return "出错了！"

@userbp.route("/active/<userid>")
def activeuser(userid):
    try:
        serUtil = TimedJSONWebSignatureSerializer(current_app.secret_key, expires_in=3000)
        userid = serUtil.loads(userid)["userid"]
        with sqlite3.connect("demo6.db") as con:
            cur = con.cursor()
            cur.execute("update user set is_active = 1 where id = ?", (userid,))
            con.commit()
        return redirect("/login/")

    except SignatureExpired:
        return "激活超时了！"
    except BadSignature:
        return "秘钥错误！"
    except Exception as error:
        print(error)
        return "出现未知错误！"

