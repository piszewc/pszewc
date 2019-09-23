from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .forms import PostForm
from .models import Post, Book
from django.utils import timezone
from django.conf import settings

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts, 'nbar': 'post_list'})

def post_detail(request, pk, slug):
    post = get_object_or_404(Post, pk=pk, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

def about_page(request):
    return render(request, 'main/about_page.html', {'nbar': 'about_page'})

def landing_page(request):
    if request.method == 'POST':
        message = request.POST['message']
        name = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        context = {'name': name, 'subject': subject,
                    'email': email,  'message': message}
        template = render_to_string(
            'main/email_template.html', context)
        send_mail('Landing Page', template, settings.EMAIL_HOST_USER,
                    ['pszewc@zoho.eu'], fail_silently=False)

    return render(request, 'main/landing_page.html', {'nbar': 'landing_page'})

def model_implementation_page(request):
    return render(request, 'other/machine_learning_model.html', {'nbar': 'model_implementation_page'})

def book_list(request):
    books = Book.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'books/book_list.html', {'books': books , 'nbar': 'book_list'})


def contact_page(request):
    if request.method == 'POST':
        message = request.POST['message']
        name = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        context = {'name': name, 'subject': subject,
                   'email': email,  'message': message}
        template = render_to_string(
            'main/email_template.html', context)
        send_mail('Contact Form', template, settings.EMAIL_HOST_USER,
                  ['pszewc@zoho.eu'], fail_silently=False)

    return render(request, 'main/contact_page.html', {'nbar': 'contact_page'})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk, slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk, slug):
    post = get_object_or_404(Post, pk=pk, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk, slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


from django.shortcuts import render
import os
import pandas as pd
from django.http import JsonResponse
from sklearn.externals import joblib

CURRENT_DIR = os.path.dirname(__file__)
model_file = os.path.join(CURRENT_DIR, 'C:/Users/piotr/Documents/GitHub/VirtualBox/pszewc/upload/media/models/saved_model.pkl')

model = joblib.load(model_file)
# Create your views here.
def api_sentiment_pred(request):
    review = request.GET['review']
    review_list = [review[0],review[2],review[4],review[6],review[8],review[10],review[12],review[14]]
    user_input_df = pd.DataFrame(columns = ["Pclass","Sex","Age","Fare","Embarked","Title","IsAlone","Age*Class"])
    user_input_df.loc[len(user_input_df), :] = review_list

    model_result = model.predict(user_input_df)

    result = 'Positive' if model_result == 1 else 'Negative'
    return (JsonResponse(result, safe=False))