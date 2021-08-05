from django.shortcuts import render
from .models import Pokemon
from django.db.models import Q
from django.http import JsonResponse
from django.core.paginator import Paginator
# pokeLab\pokeappi\views.py
# pokeLab\pokeappi\management\commands\pokemon.py

def index(request):
    return render(request, 'pokeappi/pokeappi.html')


def pokeappi(request):

    search_term = request.GET.get('search_term', '')
    page = request.GET.get('page', '1')
    page = int(page) if page.isdigit() else 1
    limit = request.GET.get('limit', '3')
    limit = int(limit) if limit.isdigit() else 3



    pokedata = Pokemon.objects.all().order_by('id').filter(Q(name__icontains=search_term)|Q(types__icontains=search_term))

    paginator = Paginator(pokedata, limit)
    if page > paginator.num_pages:
        pokedata = []
    else:
        pokedata = paginator.page(page)

    pokedex =[]
    for pokemon in pokedata:
            pokedex.append({
                'name' : pokemon.name,
                'number' : pokemon.number,
                'height' : pokemon.height,
                'weight' : pokemon.weight,
                'image_front': pokemon.image_front,
                'image_back': pokemon.image_back,
                'types': pokemon.types.split()
                })
    
    return JsonResponse({"pokedex":pokedex, 'total_pages': paginator.num_pages})

    # paginator = Paginator(pokemon, limit)
    
    # if page > paginator.num_pages:
    #     pokemon = []
    # else:
    #     pokemon = paginator.page(page)

    # pokeshortlist = []


 
# get request
# 