from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogpost')
    public = models.BooleanField()
    date_created = models.DateTimeField()

    def __str__(self):
        return self.title + ' (' + self.user.username + ')'