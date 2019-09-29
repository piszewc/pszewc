# sitemaps.py
from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return ['landing_page','book_list', 'about_page', 'contact_page']

    def location(self, item):
        return reverse(item)