# from tasks import dosomething
#
# if __name__ == '__main__':
#     # dosomething()
#     # dosomething()
#     # dosomething()
#
#     r1 = dosomething.delay()
#     r2 = dosomething.delay()
#     r3 = dosomething.delay()
#     r4 = dosomething.delay()
#     print("所有任务完工了",r1,r2,r3,r4)

# 纯粹 SQL语句  写起来麻烦  但是执行效率高
# 使用ORM框架   使用面向对象的写法  书写方便  但是执行效率低 (需要有一个将ORM语句编译成原生SQL过程)
from factory import create_app
from models import *

if __name__ == '__main__':
    app = create_app()

    # 删除所有表
    # db.drop_all()
    # 生成所有表
    # db.create_all()

    # 操作数据库不需要运行项目
    app.run(debug=True)
