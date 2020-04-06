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
from rest_framework import mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

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

class UsersViewSets(viewsets.GenericViewSet,mixins.CreateModelMixin, mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):

    queryset = User.objects.all()
    # serializer_class = UserSerializer

    def get_serializer_class(self):
        #print("action代表http方法",self.action)
        if self.action == "create":
            return UserRegisterSerializer
        return UserSerializer
