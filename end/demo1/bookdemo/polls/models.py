from django.db import models

# Create your models here.
class Poll(models.Model):
    poll_title = models.CharField(max_length=20)
    num1 = models.CharField(max_length=5,default=0)
    num2 = models.CharField(max_length=5,default=0)
    num3 = models.CharField(max_length=5,default=0)
    num4 = models.CharField(max_length=5,default=0)

    def __str__(self):
        return self.poll_title
    def __int__(self):
        return self.num1,self.num2,self.num3,self.num4