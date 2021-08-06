from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import PokemonInfo


def index(request):
    return render(request, 'poke_app/index.html')


def pokemon(request):

    pokemon = PokemonInfo.objects.all()
    pokemon_data = []
    for pokemons in pokemon:
        pokemon_data.append({
            'number': pokemons.number,
            'name': pokemons.name,
            'height': pokemons.height,
            'weight': pokemons.weight,
            'image_front': pokemons.image_front,
            'image_back': pokemons.image_back,
            'types': pokemons.types

        })
    return JsonResponse({'pokemon':pokemon_data})
   
    # return HttpResponse('yo')


