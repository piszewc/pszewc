from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .forms import PostForm
from .models import Post
from django.utils import timezone
from django.conf import settings

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def contact_page(request):
    if request.method == 'POST':
        message = request.POST['message']
        name = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        context = {'name': name, 'subject': subject,
                   'email': email,  'message': message}
        template = render_to_string(
            'blog/email_template.html', context)
        send_mail('Contact Form', template, settings.EMAIL_HOST_USER,
                  ['pszewc@zoho.eu'], fail_silently=False)

    return render(request, 'blog/contact_page.html', {'nbar': 'contact_page'})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})