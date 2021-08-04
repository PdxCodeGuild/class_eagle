from django.db import models

# Create your models here.
class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length = None)
    height = models.FloatField()
    weight = models.FloatField()
    image_front = models.CharField(max_length = None)
    image_back = models.CharField(max_length = None)
    types = models.CharField(max_length = None)