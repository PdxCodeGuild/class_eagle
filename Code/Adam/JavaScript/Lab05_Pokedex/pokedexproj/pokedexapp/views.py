from django.shortcuts import render
from django.http import JsonResponse
from .models import Pokemon

def index(request):
    return render(request, 'pokedexapp/index.html')

def pokemon(request):
    all_pokemon = Pokemon.objects.all().order_by('id')
    pokemon_data = []
    for pokemon in all_pokemon:
        print(pokemon)
        pokemon_data.append({
            'number': pokemon.number,
            'name': pokemon.name,
            'height': pokemon.height,
            'weight': pokemon.weight,
            'image_front': pokemon.image_front,
            'image_back': pokemon.image_back,
            'types': pokemon.types
        })

    return JsonResponse({'pokemon': pokemon_data})