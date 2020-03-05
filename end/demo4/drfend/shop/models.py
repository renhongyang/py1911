from django.db import models
# 使用django自带的用户系统
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20,verbose_name="分类名")

    def __str__(self):
        return self.name

class Good(models.Model):
    name = models.CharField(max_length=20,verbose_name="商品名字")
    desc = models.CharField(max_length=100,null=True,blank=True,verbose_name="商品描述")
    # 在序列化关联模型时一定要声明related_name
    # 一找多 related_name 没有定义  c1.good_set.all()   related_name定义了  c1.goods.all()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="分类",related_name='goods')

    def __str__(self):
        return self.name

class GoodImgs(models.Model):
    img = models.ImageField(upload_to='goodimg',verbose_name="商品展示图")
    good = models.ForeignKey(Good,on_delete=models.CASCADE,verbose_name="商品",related_name='imgs')

    def __str__(self):
        return self.good.name

class User(AbstractUser):
    """
    自定义用户类继承django自带用户系统
    """
    telephone = models.CharField(max_length=20, verbose_name="手机号")

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    good = models.ManyToManyField(Good,verbose_name="商品")

    def __str__(self):
        return self.user.username + "的订单"


