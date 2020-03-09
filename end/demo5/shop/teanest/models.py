from django.db import models
# 使用django自带的用户系统
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Ads(models.Model):
    img = models.ImageField(upload_to='ads', verbose_name="轮播图")
    url = models.URLField(default='http://www.rhy.com',verbose_name="图片链接")

class Articles(models.Model):
    title = models.CharField(max_length=50,verbose_name="文章标题")
    url = models.URLField(default='http://www.rhy.com', verbose_name="文章链接")

class Categorys(models.Model):
    title = models.CharField(max_length=20, verbose_name="分类名称")

class Goods(models.Model):
    img = models.ImageField(upload_to='goodimg', verbose_name="商品图片")
    name = models.CharField(max_length=50, verbose_name="商品名称")
    desc = models.CharField(max_length=100, verbose_name="商品描述")
    price = models.FloatField(default=0, verbose_name="商品价格")
    sellnum = models.PositiveIntegerField(default=0, verbose_name="商品销量")
    category = models.ForeignKey(Categorys, on_delete=models.CASCADE, verbose_name="商品分类")

class Indexcategorys(models.Model):
    title = models.CharField(max_length=20, verbose_name="分类名称")
    img = models.ImageField(upload_to='indexcateimg', verbose_name="主页分类图片")


class Indexgoods(models.Model):
    img = models.ImageField(upload_to='goodimg', verbose_name="商品图片")
    name = models.CharField(max_length=50, verbose_name="商品名称")
    desc = models.CharField(max_length=100, verbose_name="商品描述")
    price = models.FloatField(default=0, verbose_name="商品价格")
    category = models.ForeignKey(Categorys, on_delete=models.CASCADE,verbose_name="商品分类")

class Timegoods(models.Model):
    img = models.ImageField(upload_to='goodimg', verbose_name="商品图片")
    name = models.CharField(max_length=50, verbose_name="商品名称")
    desc = models.CharField(max_length=100, verbose_name="商品描述")
    price = models.FloatField(default=0, verbose_name="商品价格")
    old_price = models.FloatField(default=0, verbose_name="商品最初价格")
    category = models.ForeignKey(Categorys, on_delete=models.CASCADE,verbose_name="商品分类")


class User(AbstractUser):
    telephone = models.CharField(max_length=11, verbose_name="手机号")
