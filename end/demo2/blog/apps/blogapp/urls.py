# 引入路由绑定函数
from django.conf.urls import url
from . import views
from django.views.generic.base import RedirectView
from .feed import ArticleFeed
app_name = "blogapp"

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^single/(\d+)/$', views.single, name='single'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^rss/$',ArticleFeed(), name="rss"),
    #url(r'^single/$', views.single, name='single'),
    # url(r'^favicon/$', views.favicon),
    url(r'^favicon.ico$',RedirectView.as_view(url=r'static/img/favicon.ico')),

]