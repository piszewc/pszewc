from django.conf import settings
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify

class Categories(models.Model):
  """Post Categories"""

  name = models.CharField(max_length=100)
  description = models.CharField(max_length=400, blank=True, null=True)
  
  def __str__(self):
    return self.name

class Post(models.Model):
  """Model For Posts"""

  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  categories = models.ManyToManyField('Categories')
  
  title = models.CharField(max_length=140)
  slug = models.SlugField(max_length=140 , blank=True, null=True)

  excerpt = models.CharField(max_length=300, blank=True, null=True)
  text = models.TextField()
  
  post_image = models.ImageField(
    upload_to='post_image/', blank=True, null=True)
    
  created_date = models.DateTimeField(default=timezone.now)
    
  published_date = models.DateTimeField(blank=True, null=True)
  
  def publish(self):
    self.published_date = timezone.now()
    self.save()
    
  def __str__(self):
    return self.title

  def save(self, *args, **kwargs):
    if not self.id:
      self.slug = slugify(self.title)
    super(Post, self).save(*args, **kwargs)


class Author(models.Model):
  """Model class for authors"""

  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  
  def __str__(self):
    return self.first_name + " " + self.last_name


class Book(models.Model):
  """Model class for books"""
  
  title = models.CharField(max_length=200)
  author = models.ManyToManyField('Author')
  description = models.TextField(blank=True, null=True)

  book_image = models.ImageField(upload_to='book_cover/', blank=True, null=True)
  publication_date = models.DateTimeField(blank=True, null=True)
  published_date = models.DateTimeField(default=timezone.now)
  
  def __str__(self):
    return self.title
 