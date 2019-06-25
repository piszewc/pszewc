from django import forms

from .models import Post, Categories, Book, Author
from .models import Categories

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', "categories", "excerpt", "post_image")

class PostCategories(forms.ModelForm):

    class Meta:
        model = Categories
        fields = ('name', 'description',)


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title', 'description','author', 'book_image',)


class BookAuthor(forms.ModelForm):

    class Meta:
        model = Author
        fields = ('first_name', 'last_name',)