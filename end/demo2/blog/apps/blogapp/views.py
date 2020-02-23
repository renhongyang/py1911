from django.shortcuts import render,redirect,reverse
from django.template import loader
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
# Django自带了分页与分页器
from django.core.paginator import Paginator,Page
from .forms import CommentForm
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
    if request.method =="GET":
        try:
            #return HttpResponse("文章详情")
            article = Article.objects.get(id=articleid)
            cf=CommentForm()
            return render(request, 'single.html', locals())
        except Exception as error:
            #print(error)
            return HttpResponse("文章不符合规定！")
    elif request.method == "POST":
        cf = CommentForm(request.POST)
        if cf.is_valid():
            comment = cf.save(commit=False)
            comment.article = Article.objects.get(id=articleid)
            comment.save()
            url = reverse("blogapp:single",args=(articleid,))
            return redirect(to=url)
        else:
            article = Article.objects.get(id=articleid)
            cf = CommentForm()
            errors = "输入信息有误！"
            return render(request, 'single.html', locals())




def contact(request):
    #return HttpResponse("文章评论")
    return render(request,'contact.html')

# def favicon(request):
# #     return redirect(to="/static/favicon.ico")