from django.shortcuts import render,redirect,reverse
from django.template import loader
from django.http import HttpResponse
from django.views.generic import View,TemplateView,ListView,CreateView,DetailView,DeleteView,UpdateView
from .models import Poll,Question,Choices,User
from django.contrib.auth import authenticate,login as lin,logout as lot
from .forms import *

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
        print("当前用户",request.user.username)
        if request.user and request.user.username != "":
            # 已经登录
            # print(request.user.questions,type(request.user.questions.all()))
            try:
                question = Question.objects.get(id=qid)
                if question in request.user.questions.all():
                    #print("已经投过票")
                    url = reverse("polls:result",args=(qid,))
                    return redirect(to=url)
                else:
                    try:
                        #print(question)
                        return render(request, 'polls/detail.html', {"question": question})

                    except Exception as e:
                        print(e)
                        return HttpResponse("问题不符合规定")

            except Exception as e:
                print(e)
        else:
            url = reverse("polls:login")+"?next=/polls/detail/"+qid+"/"
            #url next拼接
            return redirect(to=url)

    elif request.method == "POST":
        choiceid = request.POST.get("num")
        try:
            choice = Choices.objects.get(id=choiceid)
            choice.votes += 1
            choice.save()
            request.user.questions.add(Question.objects.get(id=qid))
            # 返回当前投票问题的投票结果页
            url = reverse("polls:result", args=(qid,))

            return redirect(to=url)

        except:
            return HttpResponse("选项不符合规定")


def result(request,qid):

    try:
        question = Question.objects.get(id=qid)
        return render(request,'polls/result.html',{"question":question})

    except Exception as e:
        print(e)
        return HttpResponse("结果不符合规定")

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

            return redirect(to=url)

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

def login(request):
    if request.method == "GET":
        #第2种方法，使用表单类生成一个表单
        lf=LoginForm()
        return render(request, 'polls/login.html', {"lf": lf})
        #第1种方法
        #return render(request,'polls/login.html',{"errors":"用户名和密码不匹配！"})
    elif request.method == "POST":
        # 第1种方法
        # username = request.POST.get("username")
        # password = request.POST.get("password")
        #第2种方法
        lf=LoginForm(request.POST)
        if lf.is_valid():
            username = lf.cleaned_data["username"]
            password = lf.cleaned_data["password"]
        #认证成功返回用户信息，是不返回None
            user=authenticate(username=username,password=password)
        #为了生成Cookie信息
            if user:
                lin(request,user)
                next = request.GET.get("next")
                #print("取得next参数为", next)
                if next:
                    url = next
                else:
                    url = reverse("polls:index")
                return redirect(to=url)
            else:
                # url = reverse("polls:login")
                # return redirect(to=url)
                return render(request, 'polls/login.html', {"errors": "用户名和密码不匹配！"})
        else:
            return HttpResponse("出现未知错误！")

def regist(request):
    if request.method == "GET":
        # 第3种方法使用模型表单类
        # rf = RegistForm()
        # return render(request,'polls/regist.html',{"rf":rf})
        # 1使用html标签生成表单
        return render(request, 'polls/regist.html')
    else:
        username=request.POST.get("username")
        password = request.POST.get("password")
        password1 = request.POST.get("password1")
        if User.objects.filter(username=username).count()>0:
            #return  HttpResponse("用户名已存在！")
            return render(request, 'polls/regist.html', {"errors": "用户名已存在！"})
        else:
            if password != password1:
                #return HttpResponse("两次输入的密码不一致！")
                return render(request, 'polls/regist.html', {"errors": "两次输入的密码不一致！"})
            else:
                User.objects.create_user(username=username,password=password)
                url = reverse("polls:login")
                return redirect(to=url)

        # rf = RegistForm(request.POST)
        # if rf.is_valid():
        #     print(rf,rf.cleaned_data["username"])
        #     username = rf.cleaned_data["username"]
        #     password = rf.cleaned_data["password"]
        #     password2 = rf.cleaned_data["password2"]
        #     if User.objects.filter(username=username).count()>0:
        #         # return HttpResponse("用户名已存在")
        #         return render(request, 'polls/regist.html',{"errors":"用户名已存在"})
        #     else:
        #         if password == password1:
        #             # User.objects.create_user(username=username, password=password)
        #             rf.save()
        #             url = reverse("polls:login")
        #             return redirect(to=url)
        #         else:
        #             return render(request, 'polls/regist.html', {"errors": "两次输入密码不一致"})
        #             # return HttpResponse("两次输入密码不一致")
        # else:
        #     return HttpResponse("出现未知错误")


def logout(requset):

    lot(requset)
    url=reverse("polls:index")
    return redirect(to=url)
