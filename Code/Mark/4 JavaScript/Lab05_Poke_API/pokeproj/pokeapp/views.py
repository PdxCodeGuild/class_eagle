from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Pokemon

def index(request):
    return render(request, 'pokeapp/index.html')

def pokedex(request):
    poke_data = Pokemon.objects.all()
    pokedex_data = []
    for monster in poke_data:
        pokedex_data.append({
            'name' : monster.name,
            'number' : monster.number,
            'height' : monster.height,
            'weight' : monster.weight,
            'image_front': monster.image_front,
            'image_back': monster.image_back,
            'types': monster.types.split()})
    return JsonResponse({'pokedex':pokedex_data})