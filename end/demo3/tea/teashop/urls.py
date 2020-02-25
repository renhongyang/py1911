# 引入路由绑定函数
from django.conf.urls import url
from . import views
from django.views.generic.base import RedirectView

app_name = "teashop"

urlpatterns = [

    url(r'^$', views.index, name='index'),
    #url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^introduction/$', views.introduction, name='introduction'),

    url(r'^favicon.ico$',RedirectView.as_view(url=r'static/favicon.ico')),

]