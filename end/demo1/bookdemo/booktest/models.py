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



