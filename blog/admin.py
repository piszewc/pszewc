from django.contrib import admin
from .models import Post, Categories, Author, Book


admin.site.register(Post)
admin.site.register(Categories)
admin.site.register(Author)
admin.site.register(Book)