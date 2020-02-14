from django.conf.urls import url
from .import views
app_name = 'booktest'
urlpatterns = [

    url(r'^$', views.index,name='index'),
    url(r'^list/$', views.list,name='list'),
    url(r'^about/$', views.about,name='about'),
    url(r'^detail/(\d+)/$', views.detail,name='detail'),
    url(r'^deletebook/(\d+)/$', views.deletebook,name='deletebook'),

]
