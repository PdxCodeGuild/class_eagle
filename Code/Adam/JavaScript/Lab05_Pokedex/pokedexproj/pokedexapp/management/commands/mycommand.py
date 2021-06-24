from Code.Adam.JavaScript.Lab05_Pokedex.pokedexproj.pokedexapp.models import Pokemon
from django.core.management.base import BaseCommand
import json
from pokedexapp.models import Pokemon

class Command(BaseCommand):

    def handle(self, *args, **options):
        Pokemon.objects.all().delete()
        with open('pokedexapp/management/commands/pokemon.json') as file:
            text = file.read()
            data = json.loads(text)
            all_pokemon_data = data['pokemon']
            for pokemon_data in all_pokemon_data:
                number = pokemon_data['number']
                name = pokemon_data['name']
                height = pokemon_data['height']
                weight = pokemon_data['weight']
                image_front = pokemon_data['image_front']
                image_back = pokemon_data['image_back']
                types = pokemon_data['types']
                pokemon = Pokemon(
                    number=number, 
                    name=name, 
                    height=height, 
                    weight=weight,
                    image_front=image_front,
                    image_back=image_back,
                    types=types)
                pokemon.save()