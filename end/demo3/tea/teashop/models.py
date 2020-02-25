from django.db import models

# Create your models here.

class Ads(models.Model):
    img = models.ImageField(upload_to='ads',verbose_name="图片")
    desc = models.CharField(max_length=20,null=True,blank=True,verbose_name="图片描述")

    def __str__(self):
        return self.desc

class Activity(models.Model):
    title = models.CharField(max_length=5 ,default="标题",verbose_name="活动标题")
    img = models.ImageField(upload_to='activity', verbose_name="图片")
    desc = models.CharField(max_length=20, null=True, blank=True, verbose_name="图片描述")

    def __str__(self):
        return self.title

class Recommend(models.Model):
    img = models.ImageField(upload_to='recommend', verbose_name="图片")
    desc1 = models.CharField(max_length=20, null=True, blank=True, verbose_name="图片描述1")
    desc2 = models.CharField(max_length=20, null=True, blank=True, verbose_name="图片描述2")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

    # def __str__(self):
    #     return self.desc1,self.desc2


class Category(models.Model):
    name = models.CharField(max_length=20,verbose_name="分类名")
    img = models.ImageField(upload_to='category', verbose_name="图片")

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=20,verbose_name="标签名")

    def __str__(self):
        return self.name

class Goods(models.Model):
    title = models.CharField(max_length=30, verbose_name="商品名称")
    img = models.ImageField(upload_to='goods', verbose_name="图片")
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name="分类")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    price = models.FloatField(default=0, verbose_name="商品价格")
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=20, verbose_name="评论人")
    body = models.CharField(max_length=500, verbose_name="评论内容")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="评论时间")
    good = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="所属商品")

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=12,default="admin",verbose_name="用户名")
    telephone = models.CharField(max_length=11,verbose_name="手机号")
    password = models.CharField(max_length=15,verbose_name="密码")
    email = models.EmailField(default="1751522491@qq.com")
    goods = models.ManyToManyField("Goods",related_name="goods")

    def __str__(self):
        return self.username