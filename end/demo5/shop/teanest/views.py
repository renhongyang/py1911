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

class AdsViewSets(viewsets.ModelViewSet):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializers