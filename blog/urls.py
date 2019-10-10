from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap, Post_Sitemap

sitemaps = {
    'post': Post_Sitemap(),

    'static': StaticViewSitemap,
}

urlpatterns = [

    path('blog/', views.post_list, name='post_list'),
    path('blog/post/<slug:slug>-<int:pk>', views.post_detail, name='post_detail'),
    path('blog/post/new', views.post_new, name='post_new'),
    path('blog/post/<slug:slug>-<int:pk>/edit', views.post_edit, name='post_edit'),

    path('resources', views.resources, name='resources'),
    
    path('model_implementation_page', views.model_implementation_page, name='model_implementation_page'),
    path('contact', views.contact_page, name='contact_page'),
    path('about', views.about_page, name='about_page'),
    path('', views.landing_page, name='landing_page'),

    path('api/predict', views.api_sentiment_pred, name='api_sentiment_pred'), 
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)