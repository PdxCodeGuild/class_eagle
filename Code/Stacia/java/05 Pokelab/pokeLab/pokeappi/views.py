from django.shortcuts import render
from .models import Pokemon
from django.http import JsonResponse
# pokeLab\pokeappi\views.py
# pokeLab\pokeappi\management\commands\pokemon.py

def index(request):
    return render(request, 'pokeappi/pokeappi.html')


def pokeappi(request):
    poke_data = Pokemon.objects.all()
    pokedex_data = []
    for pokemon in poke_data:
        pokedex_data.append({
            'name' : pokemon.name,
            'number' : pokemon.number,
            'height' : pokemon.height,
            'weight' : pokemon.weight,
            'image_front': pokemon.image_front,
            'image_back': pokemon.image_back
       
            # 'type': pokemon.type
            })
    return JsonResponse({'poke_data':pokedex_data})
