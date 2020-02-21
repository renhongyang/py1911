from django.template import Library
from ..models import Article,Category,Tag


register=Library()
#自定义过滤器
@register.filter
def dateFormat(data):
    return "%d-%d-%d"%(data.year,data.month,data.day)

@register.filter
def authorFormat(author,info):
    return info+":"+author.upper()

#自定义标签
@register.simple_tag
def get_latestarticles(num=3):
    return Article.objects.all().order_by("-create_time")[:num]

@register.simple_tag
def get_latestdates(num=3):
    #DESC表示降序
    dates = Article.objects.dates("create_time","month","DESC")[:num]
    return dates

@register.simple_tag
def get_categorys():
    return Category.objects.all().order_by("-id")

@register.simple_tag
def get_tags():
    return Tag.objects.all().order_by("-id")



