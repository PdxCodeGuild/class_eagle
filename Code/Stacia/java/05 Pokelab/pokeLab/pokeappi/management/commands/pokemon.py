from django.core.management.base import BaseCommand
from ... models import Pokemon

import json


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('pokeappi/management/commands/pokemon.json') as file:
            text = file.read()
            data = json.loads(text)
            print(data)
            #^ use the json library to parse the raw response
            pokedex = data['pokemon']
            # ^ python dictionary
            # print(pokedex)
            for pokemon  in pokedex:
                number= pokemon['number']
                name= pokemon['name']  
                height= pokemon['height']
                weight= pokemon['weight']
                image_front= pokemon['image_front']
                image_back= pokemon['image_back']
                types= pokemon['types']
                # print(type(img_front))
                pokemon = Pokemon.objects.create(number= number, name =name ,  height = height, weight = weight, image_front = image_front, image_back = image_back, types = types)
                # print(number, name , height , weight)
                # print(pokemon)