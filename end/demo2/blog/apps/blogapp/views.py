from django.shortcuts import render
from django.template import loader
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def index(request):
    #return HttpResponse("首页")
    return render(request,'index.html')

def single(request):
    #return HttpResponse("文章详情")
    return render(request,'single.html')

def contact(request):
    #return HttpResponse("文章评论")
    return render(request,'contact.html')