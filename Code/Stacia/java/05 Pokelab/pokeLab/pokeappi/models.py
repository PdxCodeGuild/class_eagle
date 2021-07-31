from django.db import models

# Create your models here.
from django.db import models
from django.db.models.fields import FloatField

class Pokemon(models.Model):
    number= models.IntegerField(default=0)
    name= models.CharField(max_length=50, default='')
    height= models.FloatField( default=0)
    weight= models.FloatField( default=0)
    image_front= models.CharField(max_length=5000, default='')
    image_back= models.CharField(max_length=5000, default='')
    type = models.CharField(max_length=20,  default='')
    
     
    def __str__(self):
        return self.Pokemon


# [{'number': 1, 'name': 'bulbasaur', 'height': 7, 'weight': 69, 'image_front': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png', 'image_back': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/1.png', 'types': ['poison', 'grass'], 'url': 'https://pokemon.fandom.com/wiki/bulbasaur'},