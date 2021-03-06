from django import forms

from .models import Post, Categories, Book, Author
from .models import Categories
from markdownx.models import MarkdownxFormField

class PostForm(forms.ModelForm):
    
    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]



    text = MarkdownxFormField()
    
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

    categories = forms.ModelMultipleChoiceField(queryset=Categories.objects.all(), widget=forms.SelectMultiple(attrs={
            'class':'form-control',
        }))


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