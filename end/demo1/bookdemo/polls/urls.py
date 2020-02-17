from django.conf.urls import url
from .import views
app_name = 'polls'
urlpatterns = [
    url(r'^$',views.index,name='index'),
    # url(r'^polls/$',views.IndexView.as_view(),name='index'),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
    # url(r'^polls/detail/(?P<qid>\d+)/$',views.DetailView.as_view(),name='detail'),
    url(r'^result/(\d+)/$',views.result,name='result'),
    # url(r'^polls/result/(\d+)/$',views.ResultView.as_view(),name='result'),

    # url(r'^polls/$', views.poll_index,name='poll_index'),
    # url(r'^polls/detail/(\d+)/$', views.poll_detail,name='poll_detail'),
    # url(r'^polls/show/(\d+)/$', views.poll_show,name='poll_show'),
    url(r'^test/$', views.test,name='test'),
]