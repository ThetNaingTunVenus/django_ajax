from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField()
    avatar = models.ImageField(upload_to='avatar', blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Posts(models.Model):
    title = models.CharField(max_length=225)
    body = models.TextField()
    liked = models.ManyToManyField(User, blank=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class AjaxList(models.Model):
    title = models.CharField(max_length=225)
    body = models.TextField()
