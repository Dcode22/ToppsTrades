from django.db import models
from profiles.models import Profile

# Create your models here.

class Thread(models.Model):
    title = models.CharField(max_length=50)
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name='threads')
    date_created = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='posts')
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name='posts')
    date_created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=1000)

class Response(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name="responses")
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name= "responses")
    date_created = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=1000)

