from django.shortcuts import render,redirect,reverse
from django.template import loader
from django.http import HttpResponse
from .models import Book, Hero

def index(requset):
    # templates=loader.get_template('index.html')
    books=Book.objects.all()
    # context={'books':books}
    # result=templates.render(context)
    # return HttpResponse(result)
    #简写
    return render(requset,'index.html',{'books':books})

def detail(requset,bookid):
    #templates=loader.get_template('detail.html')
    book=Book.objects.get(id=bookid)
    # context={'book':book}
    # result=templates.render(context)
    # return HttpResponse(result)
    return render(requset,'detail.html',{'book':book})

def deletebook(request,bookid):
    book=Book.object.get(id=bookid)
    book.delete()
    return redirect(to='/')


def list(requset):
    return HttpResponse("这里是列表页")
def about(requset):
    return HttpResponse("这里是关于页")
def jsondata(requset):
    return HttpResponse("{'name':'rhy','age':'20'}")

# Create your views here.
