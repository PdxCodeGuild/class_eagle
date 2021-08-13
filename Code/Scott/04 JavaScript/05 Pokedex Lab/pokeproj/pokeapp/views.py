from django.shortcuts import render, reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Pokemon
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'pokeapp/index.html')

def pokemon(request):
    term = request.GET.get('term','')
    pokedex_data = []
    if term == '':
        db = Pokemon.objects.all()
    else:
        db = Pokemon.objects.filter(Q(name__icontains=term)|Q(types__icontains=term))
    for pokemon in db:
        db_types = pokemon.types.split()
        types = []
        for t in db_types:
            new_t = t.replace(',', '') 
            types.append(new_t)

        pokedex_data.append({
            'name' : pokemon.name,
            'number' : pokemon.number,
            'height' : pokemon.height,
            'weight' : pokemon.weight,
            'image_front': pokemon.image_front,
            'image_back': pokemon.image_back,
            'types': types
        })
    return JsonResponse({'pokedex': pokedex_data})
