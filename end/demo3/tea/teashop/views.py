from django.shortcuts import render,redirect,reverse
from django.template import loader
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def index(request):
    #return HttpResponse("首页")
    ads = Ads.objects.all()
    #rec1 = Recommend.objects.get(id=1)
    rec = Recommend.objects.all()
    act = Activity.objects.all()
    goods = Goods.objects.all()
    category = Category.objects.all()
    #print(ads,"+++")
    #print(rec1,'===')
    return render(request,'index.html',locals())


def login(request):
    #return render(request,'login.html')
    if request.method == "GET":
         return render(request,'login.html')
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username != '' and password != '':
            url = reverse("teashop:index")
            return redirect(to=url)
        else:
            return HttpResponse("账号或者密码输入有误")


def register(request):
    #return render(request,'register.html')
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password1 = request.POST.get("password1")

        if password != password1 and username !='':
            #return HttpResponse("两次输入的密码不一致！")
            return render(request, 'register.html', {"errors": "输入有误！"})
        else:
            #User.objects.create_user(username=username ,password=password)
            url = reverse("teashop:login")
            return redirect(to=url)


def introduction(request):
    return render(request,'introduction.html')