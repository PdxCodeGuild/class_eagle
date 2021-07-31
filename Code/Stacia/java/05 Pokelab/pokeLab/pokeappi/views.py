from django.shortcuts import render
from .models import Pokemon
from django.db.models import Q
from django.http import JsonResponse
# pokeLab\pokeappi\views.py
# pokeLab\pokeappi\management\commands\pokemon.py

def index(request):
    return render(request, 'pokeappi/pokeappi.html')


def pokeappi(request):
    

    search_term = request.GET.get('search_term', '')


    poke_data = Pokemon.objects.all().order_by('id').filter(Q(name__icontains=search_term)|Q(types__icontains=search_term))

    for pokemon in poke_data:
            pokedex_data.append({
                'name' : pokemon.name,
                'number' : pokemon.number,
                'height' : pokemon.height,
                'weight' : pokemon.weight,
                'image_front': pokemon.image_front,
                'image_back': pokemon.image_back,
                'type': pokemon.type.split()
                })

    
    
    return JsonResponse({'poke_data':pokedex_data})

    # paginator = Paginator(pokemon, limit)
    
    # if page > paginator.num_pages:
    #     pokemon = []
    # else:
    #     pokemon = paginator.page(page)

    # pokeshortlist = []


 
# get request
# 