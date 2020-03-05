"""
实现自定义认证类，（登录 内容自定义）
重写Django认证方式
"""
from django.contrib.auth import backends
#引入Q查询
from django.db.models import Q
from .models import User

class MyLoginBackend(backends.BaseBackend):
    def authenticate(self, request, **kwargs):
        """
        :param request:
        :param kwargs:认证参数
        :return: 如果认证成功返回认证用户 否则返回None
        """
        #print(kwargs,"认证参数")
        username = kwargs["username"]
        password = kwargs["password"]
        #重复3个查询
        user = User.objects.filter(Q(username=username) | Q(email=username) | Q(telephone=username)).first()
        if user:
            b = user.check_password(password)
            if b:
                return user
            else:
                 None
        else:
            return None