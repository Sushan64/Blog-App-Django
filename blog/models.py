from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
  title = models.CharField(max_length = 100)
  text = models.TextField()
  meta_description = models.TextField(max_length=150, default="Blog")
  featured_image = models.ImageField(default = "1000033197.jpg", blank = True)
  created_date = models.DateTimeField(default= timezone.now())
  published_date = models.DateTimeField(blank=True, null = True)
  
  def publish(self):
    self.published_date = timezone.now()
    return self.save()
  
  def __str__(self):
    return self.title
