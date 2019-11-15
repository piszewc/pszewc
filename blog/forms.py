from django import forms

from .models import Post, Categories, Book, Author
from .models import Categories
from tinymce.widgets import TinyMCE

class PostForm(forms.ModelForm):
    
    text = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Post
        fields = ('title', "categories", "excerpt", "post_image")

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