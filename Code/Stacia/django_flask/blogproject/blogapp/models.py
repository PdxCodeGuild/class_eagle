from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    autho = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class User_Info(models.Model):
    dino = models.CharField(max_length=20)
    # username = models.ForeignKey(User,on_delete=models.PROTECT, null=True, blank=True)
    age = models.DateField(auto_now_add=True)