from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=20)
    price=models.FloatField(default=0)
    #upd_date=models.DateField(auto_now_add=True)
    upd_date = models.DateField(default="2020-2-11")
    author=models.CharField(max_length=20,default="rhy")
    desc=models.CharField(max_length=50,null=True,blank=True,db_column="description")

    def __str__(self):
        return self.title

class Hero(models.Model):
    name=models.CharField(max_length=20)
    gender=models.CharField(max_length=6,choices=(('male','男'),('female','女')),default='male')
    content=models.CharField(max_length=100)
    book=models.ForeignKey(Book, on_delete=models.CASCADE,related_name= 'heros')

    def __str__(self):
        return self.name

class UserManager(models.Manager):

   """
   自定义模型管理类，该模型不在具有objects对象
   """
   def deleteByTelephone(self,tele):
       #django默认的objects是manager类型 *.objects.get
       user=self.get(telephone=tele)
       user.delete()

   def createUser(self,tele):
       #sele.model 可以获取模型类构造函数
       user=self.model()
       #user=user()
       user.telephone=tele
       user.save()

class User(models.Model):
    telephone=models.CharField(max_length=11,null=True,blank=True,verbose_name="手机号码")
    #自定义管理字段后不在有objects对象，自定义了一个新的objects
    objects=UserManager()
    def __str__(self):
        return self.telephone
    class Meta():
        db_table="用户类"
        ordering=["-telephone"]
        verbose_name="用户类型类a"
        verbose_name_plural="用户类型类s"

class Account(models.Model):
    username = models.CharField(max_length=20,verbose_name="用户名")
    password = models.CharField(max_length=20, verbose_name="用户密码")
    regist_date = models.DateField(verbose_name="用户注册日期",default="2020-2-15")
    #concact = models.OneToOneField('Concact',on_delete=models.CASCADE)

class Concact(models.Model):
    telephone = models.CharField(max_length=11, verbose_name="用户手机号")
    email = models.EmailField(default="1751522491@qq.com", verbose_name="用户邮箱")
    concact = models.OneToOneField('Account', on_delete=models.CASCADE,related_name='con')

class Article(models.Model):
    title=models.CharField(max_length=20,verbose_name="标题")
    summary=models.TextField(verbose_name="内容")

class Tag(models.Model):
    name=models.CharField(max_length=10,verbose_name="标签名")
    article=models.ManyToManyField('Article',related_name='tags')






