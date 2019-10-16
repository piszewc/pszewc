# sitemaps.py
from django.contrib import sitemaps
from django.urls import reverse

from .models import Post

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['landing_page','post_list' ,'resources', 'about_page', 'contact_page']

    def location(self, item):
        return reverse(item)

class Post_Sitemap(sitemaps.Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return Post.objects.all()

    def location(self, obj):
        path = "/blog/post/"+obj.slug+"-"+str(obj.id)
        return path

    def lastmod(self, obj): 
        return obj.published_date