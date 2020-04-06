"""webshop URL Configuration

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
from django.urls import path, include
from juncinet.views import *
from django.conf.urls import url
from django.views.static import serve
from .settings import MEDIA_ROOT
from rest_framework_simplejwt.views import token_obtain_pair,token_refresh
# 引入API文档路由
from rest_framework.documentation import include_docs_urls

# 引入DRF自带的路由类
from rest_framework import routers
router = routers.DefaultRouter()

# 可以通过router默认路由注册资源
router.register('ads', AdsViewSets)
router.register('articles', ArticlesViewSets)
router.register('categorys', CategoryViewSets)
router.register('goods', GoodsViewSets)
router.register('indexcategory', IndexcategorysViewSets)
router.register('indexgoods', IndexgoodsViewSets)
router.register('timegoods', TimegoodsViewSets)
router.register('users', UsersViewSets)
router.register('orders', OrdersViewSets)

urlpatterns = [
    path('admin/', admin.site.urls),
    # 配置RestFulAPI
    path('api/v1/',include(router.urls)),
    # 为了在DRF路由调试界面能够使用用户相关功能需要引入以下路由
    path('',include('rest_framework.urls')),

    url('media/(?P<path>.*)',serve, {'document_root': MEDIA_ROOT}),
    # API文档地址
    path('api/v1/docs/', include_docs_urls(title="RestFulAPI", description="RestFulAPI v1")),

    # 先通过用户名密码 得到Token  VUE将refresh以及access保存  通过access请求服务器   通过refresh获取新的access
    url(r'^obtaintoken/$', token_obtain_pair,name='login'),
    url(r'^refreshtoken/$', token_refresh, name='refresh'),


]
