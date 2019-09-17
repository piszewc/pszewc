from django.urls import path 
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('blog/', views.post_list, name='post_list'),
    path('blog/post/<slug:slug>-<int:pk>/', views.post_detail, name='post_detail'),
    path('blog/post/new/', views.post_new, name='post_new'),
    path('blog/post/<slug:slug>-<int:pk>/edit/', views.post_edit, name='post_edit'),

    path('books/', views.book_list, name='book_list'),
    
    path('model_implementation_page/', views.model_implementation_page, name='model_implementation_page'),
    path('contact/', views.contact_page, name='contact_page'),
    path('about/', views.about_page, name='about_page'),
    path('', views.landing_page, name='landing_page'),

    path('api/predict/', views.api_sentiment_pred, name='api_sentiment_pred'), 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)