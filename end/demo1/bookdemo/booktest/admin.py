from .models import Book, Hero
from django.contrib import admin
from django.contrib.admin import ModelAdmin

# Register your models here.


class HeroInline(admin.StackedInline):
    model = Hero
    #关联个数，可更改
    extra = 1

class BookAdmin(ModelAdmin):
    # list_display显示字段
    list_display = ("title", "price", "upd_date")
    # list_filter：过滤字段，过滤框会出现在右侧
    list_filter = ["title"]
    # search_fields：搜索字段，搜索框会出现在上侧
    search_fields = ["title"]
    # list_per_page：分页，分页框会出现在下侧
    list_per_page = 5
    # 再添加书的时候可以额外添加英雄
    inlines = [HeroInline]
#
class HeroAdmin(ModelAdmin):
    list_display = ("name", "gender", "content", "book")
    # list_filter：过滤字段，过滤框会出现在右侧
    list_filter = ["name"]
    # search_fields：搜索字段，搜索框会出现在上侧
    search_fields = ("name", "book")
    # list_per_page：分页，分页框会出现在下侧
    list_per_page = 5

admin.site.register(Book,BookAdmin)

admin.site.register(Hero,HeroAdmin)