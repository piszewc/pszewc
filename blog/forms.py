from django import forms

from .models import Post, Categories, Book, Author
from .models import Categories

from ckeditor.widgets import CKEditorWidget

class PostForm(forms.ModelForm):
    
    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]



    text = forms.CharField(widget=CKEditorWidget())
    
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',

        }
    ))

    excerpt = forms.CharField(widget=forms.Textarea(
        attrs={
            'class':'form-control',
            "rows":"2",
        }
    ))


    class Meta:
        model = Post
        fields = ('title', "excerpt","text","categories", "post_image")

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