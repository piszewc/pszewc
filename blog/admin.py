from django.contrib import admin
from .models import Post
from .models import Categories


admin.site.register(Post)
admin.site.register(Categories)