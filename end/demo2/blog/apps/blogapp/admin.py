from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Ads)
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Tag)





"""
admin 给后台管理使用
admin.site.register(Question)   # 管理员可以看到模型类
class ChoiceAdmin(admin.ModelAdmin):  #可以自定义Choice的管理页面
"""
