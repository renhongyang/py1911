from django.shortcuts import render,redirect
from django.template import loader
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
# Django自带了分页与分页器
from django.core.paginator import Paginator,Page
# Create your views here.

def index(request):
    #return HttpResponse("首页")
    ads=Ads.objects.all()
    #print(ads)
    articles=Article.objects.all()
    paginator = Paginator(articles, 2)
    # 获取get请求中的页码参数  默认为1
    num = request.GET.get("pagenum", 1)
    page = paginator.get_page(num)
    return render(request, 'index.html', {"ads": ads, "page": page})


def single(request):
    #return HttpResponse("文章详情")
    return render(request,'single.html')

def contact(request):
    #return HttpResponse("文章评论")
    return render(request,'contact.html')

# def favicon(request):
# #     return redirect(to="/static/favicon.ico")