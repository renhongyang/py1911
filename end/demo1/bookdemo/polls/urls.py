from django.conf.urls import url
from .import views
app_name = 'polls'
urlpatterns = [

    url(r'^polls/$', views.poll_index,name='poll_index'),
    url(r'^polls/detail/(\d+)/$', views.poll_detail,name='poll_detail'),
    url(r'^polls/show/(\d+)/$', views.poll_show,name='poll_show'),
    url(r'^test/$', views.test,name='test'),
]