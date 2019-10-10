# sitemaps.py
from django.contrib import sitemaps
from django.urls import reverse

from .models import Post

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return ['landing_page','book_list', 'about_page', 'contact_page']

    def location(self, item):
        return reverse(item)

class Post_Sitemap(sitemaps.Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return Article.objects.all()

    def location(self, obj):
        return obj.note_full_path

    def lastmod(self, obj): 
        return obj.date_modified