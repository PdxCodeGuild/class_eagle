from django.core.management.base import BaseCommand
from poke_app.models import PokemonInfo
import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        PokemonInfo.objects.all().delete()
        with open('poke_app/management/commands/pokemon.json')as file:
            text = file.read()

        data = json.loads(text)
        pokemon_data = data['pokemon']

        for pokemons in pokemon_data:
            number = pokemons['number']
            name = pokemons['name']
            height = pokemons['height']
            weight = pokemons['weight']
            image_front = pokemons['image_front']
            image_back = pokemons['image_back']
            types = pokemons['types']
            pokemons = PokemonInfo(number=number, name=name, height=height, weight=weight, image_front=image_front, image_back=image_back, types=types)
            pokemons.save()

        print(pokemon_data[0])


    