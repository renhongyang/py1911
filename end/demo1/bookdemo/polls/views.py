from django.shortcuts import render,redirect,reverse
from django.template import loader
from django.http import HttpResponse
from django.views.generic import View,TemplateView,ListView,CreateView,DetailView,DeleteView,UpdateView
from .models import Poll,Question,Choices

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
        #上述方法未能实现更改单表同行数据，数据库中数据都会修改

def poll_show(requset,pollid):

    poll=Poll.objects.get(id=pollid)
    return render(requset,'poll_show.html',{'poll':poll})



#投票应用页面
#FBV视图类
def index(request):
    questions = Question.objects.all()
    return render(request,'polls/index.html',{"questions":questions})
    # return HttpResponse("首页")

def detail(request,qid):

    if request.method == "GET":
        try:
            question = Question.objects.get(id=qid)
            # print(question, "--")
            return render(request, 'polls/detail.html', {"question": question})

        except Exception as e:
            print(e)
            return HttpResponse("问题不符合规定")
    elif request.method == "POST":
        choiceid = request.POST.get("num")
        try:
            choice = Choices.objects.get(id=choiceid)
            choice.votes+=1
            choice.save()
            # 返回当前投票问题的投票结果页
            url = reverse("polls:result",args=(qid,))
            # 投票成功 返回投票结果
            return redirect(to=url)

        except:
            return HttpResponse("选项不符合规定")

    # return HttpResponse("详情页"+qid)

def result(request,qid):

    try:
        question = Question.objects.get(id=qid)
        return render(request,'polls/result.html',{"question":question})
    except Exception as e:
        print(e)
        return HttpResponse("问题不符合规定")

def test(requset):
    return HttpResponse("这里是测试页")

#CBV视图类

#投票应用主页面
class IndexView(ListView):

    # 方法一 继承的TemplateView
    # template_name = "polls/index.html"
    # def get_context_data(self, **kwargs):
    #     return {"questions":Question.objects.all()}

    # 方法二 继承ListView
    # template_name 指明使用的模板名
    template_name = "polls/index.html"
    # queryset 指明返回的结果列表信息
    queryset = Question.objects.all()
    # context_object_name 指明返回字典参数的键名
    context_object_name = "questions"

class DetailView(View):
    # get方法
    def get(self,request,qid):
        try:
            question = Question.objects.get(id=qid)
            # 使用render发起请求
            return render(request, 'polls/detail.html', {"question": question})

        except Exception as e:
            print(e)
            return HttpResponse("问题不符合规定")

    # post方法
    def post(self,request,qid):
        choiceid = request.POST.get("num")
        try:
            choice = Choices.objects.get(id=choiceid)
            choice.votes += 1
            choice.save()
            url = reverse("polls:result", args=(qid,))

            # redirect其实没有真正的返回内容   而是让浏览器重新请求一个地址
            # 不能反复刷新post的结果
            # question = Question.objects.get(id=qid)
            # 错误的结局  刷新页面导致数据出错
            # return render(request,'polls/result.html',{"question":question})
            return redirect(to=url)
            # return HttpResponse("投票成功了")  #接受了详情页的post请求
            # return HttpResponse("现在我代替你进入到了投票结果页")  # 接受了结果页的get请求

        except Exception as e:
            print(e)
            return HttpResponse("选项不符合规定")

class ResultView(View):
    # 方法一 继承View
    def get(self,request,qid):
        try:
            question = Question.objects.get(id=qid)
            return render(request, 'polls/result.html', {"question": question})
        except Exception as e:
            print(e)
            return HttpResponse("问题不合规定")

