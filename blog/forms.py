from django import forms

from .models import Post
from .models import Categories

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', "categories", "excerpt", "post_image")

class PostCategories(forms.ModelForm):

    class Meta:
        model = Categories
        fields = ('name', 'description',)