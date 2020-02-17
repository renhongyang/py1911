from django.shortcuts import render,redirect,reverse
from django.template import loader
from django.http import HttpResponse
from .models import Poll

# Create your views here.
def poll_index(request):

    polls=Poll.objects.all()
    return render(request,'poll_index.html',{'polls':polls})

def poll_detail(request,pollid):

    poll=Poll.objects.get(id=pollid)
    poll.num1 = int(poll.num1)
    poll.num2 = int(poll.num2)
    poll.num3 = int(poll.num3)
    poll.num4 = int(poll.num4)
    if request.method=="GET":
        return render(request, 'poll_detail.html', {'poll': poll})
    elif request.method=="POST":
        # poll.num1  = request.POST.get("choose")
        # poll.num2 = request.POST.get("choose")
        # poll.num3 = request.POST.get("choose")
        # poll.num4 = request.POST.get("choose")
        poll.num1 += 1
        poll.num2 += 1
        poll.num3 += 1
        poll.num4 += 1
        poll.save()
        url = reverse("polls:poll_show",args=(pollid,))
        return redirect(to=url)


def poll_show(requset,pollid):

    poll=Poll.objects.get(id=pollid)
    return render(requset,'poll_show.html',{'poll':poll})



def test(requset):
    return HttpResponse("这里是测试页")
