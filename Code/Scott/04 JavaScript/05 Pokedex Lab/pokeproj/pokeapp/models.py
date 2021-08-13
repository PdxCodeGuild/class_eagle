from django.db import models

# Create your models here.
class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length = 100)
    height = models.FloatField()
    weight = models.FloatField()
    image_front = models.CharField(max_length = 100)
    image_back = models.CharField(max_length = 100)
    types = models.CharField(max_length = 100)