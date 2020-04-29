from django.shortcuts import render
# Create your views here.

from rest_framework import viewsets
from .models import *
from .serializers import *
from django.http import HttpResponse
# 通过api_view装饰器可以将基于函数的视图转换成APIView基于类的视图
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.views import View
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions
from .import permissions as mypermissions
from rest_framework import mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

class AdsViewSets(viewsets.ModelViewSet):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer

class ArticlesViewSets(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer

class CategoryViewSets(viewsets.ModelViewSet):

    queryset = Categorys.objects.all()

    def get_serializer_class(self):
        return CategorysSerizlizer

class GoodsViewSets(viewsets.ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

    #filterset_fields = ["name"]
    # 局部过滤配置
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ["name"]
    search_fields = ["name"]
    ordering_fields = ["id"]

class IndexcategorysViewSets(viewsets.ModelViewSet):
    queryset = Indexcategorys.objects.all()
    serializer_class = IndexcategorysSerializer

class IndexgoodsViewSets(viewsets.ModelViewSet):
    queryset = Indexgoods.objects.all()
    serializer_class = IndexgoodsSerializer

class TimegoodsViewSets(viewsets.ModelViewSet):
    queryset = Timegoods.objects.all()
    serializer_class = TimegoodsSerializer


class OrdersViewSets(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer

    # permission_classes = [mypermissions.OrdersPermission]

    def get_permissions(self):
        """
        超级管理员只可以展示所有订单
        普通用户 可以创建修改、订单 不可以操作其他用户的订单
        :return:
        """
        # print("http方法为",self.action)
        if self.action == "create":
            return [permissions.IsAuthenticated()]
        elif self.action == "update" or self.action == "partial_update" or self.action == "retrieve" or self.action == "destroy":
            return [mypermissions.OrdersPermission()]
        else:
            return [permissions.IsAdminUser()]

@api_view(["GET"])
def getuserinfo(request):
    user = JWTAuthentication().authenticate(request)
    print("当前用户", user[0])
    seria = UserSerializer(instance=user[0])
    return Response(seria.data, status=status.HTTP_200_OK)

class UsersViewSets(viewsets.GenericViewSet,mixins.CreateModelMixin, mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):

    queryset = User.objects.all()
    # serializer_class = UserSerializer

    def get_serializer_class(self):
        # print("action代表http方法",self.action)
        if self.action == "create":
            return UserRegisterSerializer
        return UserSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["username"]





from urllib import request
from urllib import parse

import urllib.request
import time
import hashlib
import random

def getnums():
    s = ""
    for i in range(6):
        s += str( random.randrange(0,9))
    return s


@api_view(["POST"])
def sendmsg(req):
    try:
        print(req.data)
        """
        向数据库中写入数据 
        手机号 验证码  发送时间
        """
        print("python demo starting...")

        url = "https://openapi.miaodiyun.com/distributor/sendSMS"
        accountSid = "5ddd6bfa5d1195eb16d160e64d5dbb8c"
        to = req.data["telephone"]
        templateid = "241019"
        param = getnums()
        print("发送验证码为", param)
        auth_token = "cc8baf390e4f5e8ea9ee4a7df9cbd464"

        t = time.time()
        timestamp = str((int(round(t * 1000))))
        sig = accountSid + auth_token + timestamp
        m1 = hashlib.md5()
        m1.update(sig.encode("utf-8"))
        sig = m1.hexdigest()

        data = "accountSid=" + accountSid + "&to=" + to + "&templateid=" + templateid + "&param=" + param + "&timestamp=" + timestamp + "&sig=" + sig
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36'
        }
        data = str.encode(data)

        print("data sent to SMS server is:")
        print(data)
        req = request.Request(url, headers=headers, data=data)  # POST方法
        page = request.urlopen(req).read()
        page = page.decode('utf-8')
        print("response from SMS server is:")
        print(page)

        print("python demo finished")

        # ver = Verify()
        # ver.code=param
        # ver.telephone=to
        # ver.save()

        return Response("发送成功")


    except Exception as e:
        print(e)
        return Response(status=status.HTTP_400_BAD_REQUEST)

