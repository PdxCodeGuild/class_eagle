from django.db import models

class Message(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, default='Anonymous')
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author + ' - ' + self.body[:20] + '...'
