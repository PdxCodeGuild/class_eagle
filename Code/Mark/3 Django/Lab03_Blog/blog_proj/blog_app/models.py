from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=300, null=True)
    profile_image = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.user.username

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogpost')
    public = models.BooleanField()
    date_created = models.DateTimeField()
    date_edited = models.DateTimeField(null=True)

    def __str__(self):
        return self.title + ' (' + self.user.username + ')'