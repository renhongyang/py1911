from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Question,Choices
# Register your models here.
class ChoiceInline(admin.StackedInline):
    # 关联的模型类
    model = Choices
    # 关联个数
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    # list_display = [""]
    inlines = [ChoiceInline]

class ChoiceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choices,ChoiceAdmin)