from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=10,verbose_name="部门名称")

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=5,verbose_name="职员名称")
    salary = models.FloatField(default=999.0,verbose_name="职员薪资")
    entry_time = models.DateTimeField(auto_now_add=True,verbose_name="职员入职时间")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="职员部门", related_name='employees')

    def __str__(self):
        return self.name


