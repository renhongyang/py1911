from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.views import View
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins

# Create your views here.

class EmployeeViewSets(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DepartmentViewSets(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentViewSets(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerizlizer

    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

class EmplayeeViewSets(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerizlizer

    def get(self,request,pk):
        return self.retrieve(request,pk)

    def put(self,request,pk):
        return self.update(request,pk)

    def patch(self,request,pk):
        return self.update(request,pk)

    def delete(self,request,pk):
        return self.delete(request,pk)
