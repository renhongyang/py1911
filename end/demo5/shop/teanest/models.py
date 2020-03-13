from django.db import models
# 使用django自带的用户系统
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Ads(models.Model):
    img = models.ImageField(upload_to='ads', verbose_name="轮播图")
    url = models.URLField(default='http://www.rhy.com',verbose_name="图片链接")

class Articles(models.Model):
    title = models.CharField(max_length=50, verbose_name="文章标题")
    url = models.URLField(default='http://www.rhy.com', verbose_name="文章链接")

    def __str__(self):
        return self.title


class Categorys(models.Model):
    title = models.CharField(max_length=20, verbose_name="分类名称")

    def __str__(self):
        return self.title

class Goods(models.Model):
    img = models.ImageField(upload_to='goodimg', verbose_name="商品图片")
    name = models.CharField(max_length=50, verbose_name="商品名称")
    desc = models.CharField(max_length=100, verbose_name="商品描述")
    price = models.FloatField(default=0, verbose_name="商品价格")
    sellnum = models.PositiveIntegerField(default=0, verbose_name="商品销量")
    category = models.ForeignKey(Categorys, on_delete=models.CASCADE, verbose_name="商品分类")

    def __str__(self):
        return self.name,self.desc

class Indexcategorys(models.Model):
    title = models.CharField(max_length=20, verbose_name="分类名称")
    img = models.ImageField(upload_to='indexcateimg', verbose_name="主页分类图片")

    def __str__(self):
        return self.title


class Indexgoods(models.Model):
    img = models.ImageField(upload_to='goodimg', verbose_name="商品图片")
    name = models.CharField(max_length=100, verbose_name="商品名称")
    price = models.FloatField(default=0, verbose_name="商品价格")
    category = models.ForeignKey(Indexcategorys, on_delete=models.CASCADE,verbose_name="商品分类")

    def __str__(self):
        return self.name

class Timegoods(models.Model):
    img = models.ImageField(upload_to='goodimg', verbose_name="商品图片")
    name = models.CharField(max_length=100, verbose_name="商品名称")
    price = models.FloatField(default=0, verbose_name="商品价格")
    old_price = models.FloatField(default=0, verbose_name="商品最初价格")

    def __str__(self):
        return self.name

class Brands(models.Model):
    img = models.ImageField(upload_to='goodimg', verbose_name="品牌图片")
    name = models.CharField(max_length=50, verbose_name="品牌名称")
    category = models.ForeignKey(Categorys, on_delete=models.CASCADE, verbose_name="品牌所属分类")

    def __str__(self):
        return self.name


class User(AbstractUser):
    telephone = models.CharField(max_length=11, verbose_name="手机号")

class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    good = models.ManyToManyField(Goods,verbose_name="商品")
    num = models.PositiveIntegerField(default=0,verbose_name="购买数量")

    # def __str__(self):
    #     return self.user.username
