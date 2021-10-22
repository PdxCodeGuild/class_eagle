from django.db import models
from django.contrib.auth.models import User

class Blogpost(models.Model):
    title = models.CharField(max_length=100)
    post = models.TextField(max_length=200)
    url = models.CharField(max_length=200,null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'blogposts')
    public = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='images/',null=True, blank=True)

    def __str__(self):
        return str(self.user)




