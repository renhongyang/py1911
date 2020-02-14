from django.conf.urls import url
from .import views
app_name = 'booktest'
urlpatterns = [

    url(r'^$', views.index,name='index'),
    url(r'^list/$', views.list,name='list'),
    url(r'^about/$', views.about,name='about'),
    url(r'^detail/(\d+)/$', views.detail,name='detail'),
    url(r'^deletebook/(\d+)/$', views.deletebook,name='deletebook'),
    url(r'^editbook/(\d+)/$', views.editbook,name='editbook'),
    url(r'^addbook/$', views.addbook,name='addbook'),
    url(r'^deletehero/(\d+)/$', views.deletehero,name='deletehero'),
    url(r'^edithero/(\d+)/$', views.edithero,name='edithero'),
    url(r'^addhero/(\d+)/$', views.addhero,name='addhero'),

]
