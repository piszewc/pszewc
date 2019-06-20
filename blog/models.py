from django.conf import settings
from django.db import models
from django.utils import timezone

class Categories(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=400, blank=True, null=True)

	def __str__(self):
		return self.name

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    categories = models.ManyToManyField('Categories')

    title = models.CharField(max_length=100)
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