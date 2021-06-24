from django.core.management.base import BaseCommand
from pokeapp.models import Pokemon
import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        Pokemon.objects.all().delete()
        with open('pokeapp/management/commands/pokemon.json') as file:
            text = file.read()
        data = json.loads(text)
        pokemon_data = data['pokemon']
        for pokemon in pokemon_data:
            name = pokemon['name']
            number = pokemon['number']
            height = pokemon['height']
            weight = pokemon['weight']
            image_front = pokemon['image_front']
            image_back = pokemon['image_back']
            types = ''
            for element in pokemon['types']:
                if types != '':
                    types = types+', '+element
                else:
                    types = element
            pokemon = Pokemon(name=name,number=number,height=height,weight=weight,image_front=image_front,image_back=image_back,types=types)
            pokemon.save()
