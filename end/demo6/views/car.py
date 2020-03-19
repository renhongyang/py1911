from flask import Blueprint,render_template,request,session
from models.car import *
carbp = Blueprint("carbp",__name__)
@carbp.route("/")
# def index():
#     carlist = [
#         {"id": 101, "name": "玛莎拉蒂"},
#         {"id": 102, "name": "法拉利"},
#         {"id": 103, "name": "奥迪"}
#                ]
#     return render_template("index.html", carlist=carlist, username="rhy")
def index():

    # c = Category()
    # c.name = "炫酷跑车"
    # db.session.add(c)

    # c1 = Category()
    # c1.name = "拉风跑车"
    # db.session.add(c1)

    # c2 = Category()
    # c2.name = "豪华跑车"
    # db.session.add(c2)

    # c3 = Category()
    # c3.name = "概念跑车"
    # db.session.add(c3)
    # db.session.delete(c3)
    # db.session.commit()
    cs = Category.query.all()
    username = session.get("username")
    if username:
        return render_template("index.html", cs=cs, username=username)
    else:
        username = "无用户登录"
        return render_template("index.html", cs=cs, username=username)




@carbp.route("/categorys/<id>")
def category(id):
    car = Category.query.filter_by(id=id).first()

    if car:
        # 表关联查询
        # cs = Car.query.filter_by(cid=c.id).all()
        # cs[0].cid

        # 关系字段查询
        cars = car.cars
        # print(cs[0].category.id, cs[0].category.name)
        return render_template("category.html", cars=cars)

    return "输入不合法"