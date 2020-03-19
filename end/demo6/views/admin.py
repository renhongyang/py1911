from flask import Blueprint,render_template,request,flash,redirect,current_app,session,make_response
from models import *
from .utils import checklogin

adminbp = Blueprint("adminbp",__name__)

@adminbp.route("/admin/", methods=["GET","POST"])
@checklogin
def admin():
    # username =request.cookies.get("username")
    # username = session.get("username")
    # if username:
    cs = Category.query.all()
    cars = Car.query.all()
    return render_template("/admin/admin.html", cs=cs, cars=cars)

    # else:
    #     return redirect("/login/?next=/admin/")

@adminbp.route("/admin/<resourcetype>/add/", methods=["GET","POST"])
@checklogin
def add(resourcetype):
    if request.method == "GET":
        fields = []
        if resourcetype == "category":
            ps = dir(Category)
            for p in ps:
                if (not p.startswith("__")) and (not p.startswith("_")) and (
                        p not in ["metadata", "query", "query_class", "id", "cars"]):
                    fields.append(p)
        elif resourcetype == "car":
            ps = dir(Category)
            for p in ps:
                if (not p.startswith("__")) and (not p.startswith("_")) and (
                        p not in ["metadata", "query", "query_class", "id", "cars"]):
                    fields.append(p)
        return render_template("/admin/add.html", fs=fields)

    elif request.method == "POST":
        if resourcetype == "category":
            category = Category()
            category.name = request.form["name"]
            db.session.add(category)
            db.session.commit()

            # error = None

            # if not email:
            #     error = "邮箱不能为空！"
            # elif not password:
            #     error = "密码不能为空！"
            # elif password != password1:
            #     error = "两次输入密码不相同！"
            #
            # if error:
            #     flash(error)
            #     # return render_template("register.html")
            #     return redirect("/register/")
        elif resourcetype == "car":
            car = Car()
            car.name = request.form["name"]
            car.cid = 4
            db.session.add(car)
            db.session.commit()
        return redirect("/admin/")

@adminbp.route("/admin/<resourcetype>/delete/<id>",methods=["GET","POST"])
@checklogin
def delete(resourcetype,id):
    if resourcetype == "category":
        category = Category.query.filter_by(id=id).first()
        db.session.delete(category)
        db.session.commit()

    elif resourcetype == "car":
        c = Car.query.filter_by(id=id).first()
        db.session.delete(c)
        db.session.commit()

    return redirect("/admin/")


"""
使用装饰器限制用户操作之前需要登录
"""
