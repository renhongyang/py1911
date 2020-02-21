from django.shortcuts import render,redirect
from django.template import loader
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
# Django自带了分页与分页器
from django.core.paginator import Paginator,Page
# Create your views here.

def index(request):
    #return HttpResponse("首页")
    ads = Ads.objects.all()
    #print(ads)
    typepage = request.GET.get("type")
    year = None
    month = None
    category_id = None
    tag_id = None
    if typepage == "date":
        year = request.GET.get("year")
        month = request.GET.get("month")
        articles = Article.objects.filter(create_time__year=year, create_time__month=month).order_by("-create_time")

    elif typepage == "category":
        category_id = request.GET.get("category_id")
        try:
            category = Category.objects.get(id=category_id)
            articles = category.article_set.all()
        except Exception as error:
            #print(error)
            return HttpResponse("分类有误！")

    elif typepage == "tag":
        tag_id = request.GET.get("tag_id")
        try:
            tag = Category.objects.get(id=tag_id)
            articles = tag.article_set.all()
        except Exception as error:
            # print(error)
            return HttpResponse("分类有误！")


    else:
        articles = Article.objects.all().order_by("-create_time")

    #print(locals())可以返回作用域局部变量
    paginator = Paginator(articles, 2)
    # 获取get请求中的页码参数  默认为1
    num = request.GET.get("pagenum", 1)
    page = paginator.get_page(num)
    return render(request,'index.html',locals())
    #return render(request, 'index.html', {"ads": ads, "page": page , "year":year,"month":month,"type":typepage ,})


def single(request,articleid):
    #return HttpResponse("文章详情")
    article = Article.objects.get(id=articleid)
    return render(request,'single.html', {"article":article})

def contact(request):
    #return HttpResponse("文章评论")
    return render(request,'contact.html')

# def favicon(request):
# #     return redirect(to="/static/favicon.ico")