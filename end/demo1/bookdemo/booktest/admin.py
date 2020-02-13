from .models import Book, Hero
from django.contrib import admin
from django.contrib.admin import ModelAdmin

# Register your models here.


# class HeroInline(admin.StackedInline):
#     model = Hero
#     # 关联个数
#     extra = 1
#
# class BookAdmin(admin.ModelAdmin):
#     # list_display：显示字段，可以点击列头进行排序
#     list_display = ["title", "price", "pub_date"]
#     # list_filter：过滤字段，过滤框会出现在右侧
#     list_filter = ["title"]
#     # search_fields：搜索字段，搜索框会出现在上侧
#     search_fields = ["title"]
#     # list_per_page：分页，分页框会出现在下侧
#     list_per_page = 2
#     # 再添加书的时候可以额外添加英雄
#     inlines = [HeroInline]
#
# class HeroAdmin(admin.ModelAdmin):
#     list_display = ["name", "gender", "content", "book"]
#     # list_filter：过滤字段，过滤框会出现在右侧
#     list_filter = ["name"]
#     # search_fields：搜索字段，搜索框会出现在上侧
#     search_fields = ["name", "book"]
#     # list_per_page：分页，分页框会出现在下侧
#     list_per_page = 2

admin.site.register(Book)

admin.site.register(Hero)