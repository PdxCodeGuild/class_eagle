from django.db import models

class DadJoke(models.Model):
    joke = models.TextField()
    timestamp = models.DateTimeField()
    
    def __str__(self):
        return self.joke

