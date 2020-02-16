from django.shortcuts import render,redirect,reverse
from django.template import loader
from django.http import HttpResponse
from .models import Poll

# Create your views here.
def poll_index(requset):

    polls=Poll.objects.all()
    return render(requset,'poll_index.html',{'polls':polls})

def poll_detail(requset,pollid):

    poll=Poll.objects.get(id=pollid)
    return render(requset,'poll_detail.html',{'poll':poll})

def poll_show(requset,pollid):

    poll=Poll.objects.get(id=pollid)
    return render(requset,'poll_show.html',{'poll':poll})



def test(requset):
    return HttpResponse("这里是测试页")
