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

class Question(models.Model):
    """
    投票问题类
    """
    title = models.CharField(max_length=50, verbose_name="投票问题")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "投票表"
        verbose_name_plural = verbose_name
        ordering = ["-create_time"]

class Choices(models.Model):
    """
    投票选项类
    """
    content = models.CharField(max_length=50, verbose_name="选项")
    votes = models.PositiveIntegerField(verbose_name="得票数")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices', verbose_name="所属问题")

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "选项表"
        verbose_name_plural = "选项表"
        ordering = ["-create_time"]