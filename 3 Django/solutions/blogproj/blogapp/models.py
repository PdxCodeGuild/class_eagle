from django.db import models
from users.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    public = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    banner_image = models.ImageField(upload_to='blog_post_banners/')

    def __str__(self):
        return self.title + ' by ' + self.user.username



# default:           user.blogpost_set.all()
# with related_name: user.posts.all()