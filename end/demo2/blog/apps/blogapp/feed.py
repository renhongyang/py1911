#使用Django框架中集成的RSS包装工具
from django.contrib.syndication.views import Feed
from django.shortcuts import reverse
from .models import Article

class ArticleFeed(Feed):
    title = "web相关技术"
    description = "不时会发布一下有关web开发的技术文档"
    link = "/"

    def items(self):
        return Article.objects.all().order_by("-create_time")[:3]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.author

    def item_link(self, item):
        # return "/single/"+item.id+"/"
        url = reverse("blogapp:single", args=(item.id,))
        return url


