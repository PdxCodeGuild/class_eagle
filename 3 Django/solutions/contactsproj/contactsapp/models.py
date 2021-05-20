from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    wears_glasses = models.BooleanField()
    favorite_int = models.IntegerField()
    favorite_float = models.FloatField()
    birthday = models.DateField()

    def __str__(self):
        return self.name
        # return self.name + ' / ' + self.bio[:4]+'...'

