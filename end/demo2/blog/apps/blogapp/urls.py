# 引入路由绑定函数
from django.conf.urls import url
from . import views


app_name = "blogapp"

urlpatterns = [

    url(r'^$',views.index,name='index'),
    #url(r'^single/(\d+)/$',views.single,name='single'),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^single/$', views.single, name='single'),
]