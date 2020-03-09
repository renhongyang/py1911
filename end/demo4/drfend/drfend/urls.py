"""drfend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from shop.views import *
from django.conf.urls import url
from django.views.static import serve
from .settings import MEDIA_ROOT

# 引入API文档路由
from rest_framework.documentation import include_docs_urls

#引入restframework_simple路由
#from  rest_framework_jwt.views import obtain_jwt_token
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh

# 引入DRF自带的路由类
from rest_framework import routers
router = routers.DefaultRouter()

# 可以通过router默认路由注册资源
router.register('categorys',CategoryViewSets1)
router.register('goods',GoodViewSets)
router.register('goodimgs',GoodImgsViewSets)
router.register('users',UserViewSets)
router.register('orders',OrderViewSets)

urlpatterns = [
    path('admin/', admin.site.urls),
    # 配置RestFulAPI
    path('api/v1/',include(router.urls)),
    # 为了在DRF路由调试界面能够使用用户相关功能需要引入以下路由
    path('',include('rest_framework.urls')),

    url('media/(?P<path>.*)',serve, {'document_root': MEDIA_ROOT}),
    # url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    # API文档地址
    path('api/v1/docs/', include_docs_urls(title="RestFulAPI", description="RestFulAPI v1")),
    #url(r'^login/$', token_obtain_pair, name='login'),
    url(r'^obtaintoken/$', token_obtain_pair, name='login'),
    url(r'^refresh/$', token_refresh, name='refresh'),
    url(r'^getuserinfo/$',getuserinfo),

    # url(r'^categorylist/$',categoryList,name='categorylist'),
    # url(r'^categorydetail/(\d+)/$',categoryDetail,name='categorydetail'),

    # url 第二个参数本该是函数的引用 此处为何是函数的地址  此处as_view()  返回值其实是另外一个函数的引用(闭包)
    # url(r'^categorylist/$',CategoryListView.as_view(),name='categorylist'),
    # url(r'^categorydetail/(\d+)/$',CategoryDetailView.as_view(),name='categorydetail'),

    # url(r'^categorylist/$',CategoryListView.as_view(),name='categorylist'),
    # url(r'^categorydetail/(?P<pk>\d+)/$',CategoryDetailView.as_view(),name='categorydetail'),

    # url(r'^categorys/$',CategoryViewSets2.as_view({'get':'list','post':'create'})),
    # url(r'^categorys/(?P<pk>\d+)/$',CategoryViewSets2.as_view({'get':'retrieve','put':'update','patch':'update','delete':'destroy'})),
]
