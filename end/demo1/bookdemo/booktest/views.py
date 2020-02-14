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

def addbook(request):
    if request.method=="GET":
        return render(request,'addbook.html')
    elif request.method=="POST":
        book=Book()
        book.name=request.POST.get("booktitle")
        book.gender = request.POST.get("bookprice")
        book.upd_date=request.POST.get("bookupd_date")
        book.save()
        return redirect(to='/')

def editbook(request,bookid):
    book=Book.objects.get(id=bookid)
    book.upd_date=str(book.upd_date)
    if request.method=="GET":
        return render(request,'editbook.html',{"book":book})
    elif request.method=="POST":
        book.title = request.POST.get("booktitle")
        book.price = request.POST.get("bookprice")
        book.upd_date = request.POST.get("bookupd_date")
        book.save()
        url = reverse("booktest:index")
        return redirect(to=url)

def deletehero(request,heroid):
    hero=Hero.objects.get(id=heroid)
    bookid=hero.book.id
    hero.delete()
    url=reverse("booktest:detail",args=(bookid,))
    return redirect(to=url)

def addhero(request,bookid):
    if request.method=="GET":
        return render(request,'addhero.html')
    elif request.method=="POST":
        hero=Hero()
        hero.name=request.POST.get("heroname")
        hero.gender = request.POST.get("herosex")
        hero.content=request.POST.get("herocontent")
        hero.book=Book.objects.get(id=bookid)
        hero.save()
        url = reverse("booktest:detail", args=(bookid,))
        return redirect(to=url)

def edithero(request,heroid):
    hero=Hero.objects.get(id=heroid)
    if request.method=="GET":
        return render(request,'edithero.html',{"hero":hero})
    elif request.method=="POST":
        hero.name = request.POST.get("heroname")
        hero.gender = request.POST.get("herosex")
        hero.content = request.POST.get("herocontent")
        hero.save()
        url = reverse("booktest:detail", args=(hero.book.id,))
        return redirect(to=url)







def list(requset):
    return HttpResponse("这里是列表页")
def about(requset):
    return HttpResponse("这里是关于页")
def jsondata(requset):
    return HttpResponse("{'name':'rhy','age':'20'}")

# Create your views here.
