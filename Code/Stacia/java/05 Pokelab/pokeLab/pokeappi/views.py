from django.shortcuts import render
from .models import Pokemon

# pokeLab\pokeappi\views.py
# pokeLab\pokeappi\management\commands\pokemon.py

def pokeappi(request):
    pokemon = Pokemon.objects.all()
   
    
    return render(request, 'Pokeappi/pokeappi.html',)

def pokeappi(request):
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
            'type': monster.type})
    return JsonResponse({'pokedex':pokedex_data})
