from django.core.management.base import BaseCommand
from pokeapp.models import Pokemon
import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        Pokemon.objects.all().delete()
        
        with open('pokeapp/management/commands/pokemon.json') as file:
            text = file.read()

        data = json.loads(text)
        json_data = data['pokemon']

        for pokemon in json_data:
            name = pokemon['name']
            number = pokemon['number']
            height = round(pokemon['height']*0.1, 2)
            weight = round(pokemon['weight']*0.1, 2)
            image_front = pokemon['image_front']
            image_back = pokemon['image_back']
            types = ', '.join(pokemon['types'])

            pokemon = Pokemon(
                name = name,
                number = number,
                height = height,
                weight = weight,
                image_front = image_front,
                image_back = image_back,
                types = types
            )
            pokemon.save()