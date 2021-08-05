from django.shortcuts import render, reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Pokemon
from django.db.models import Q
from django.core.paginator import Paginator

def index(request):
    return render(request, 'pokeapp/index.html')

def pokedex(request):
    search_term = request.GET.get('search','')
    if search_term.isdigit():
        search_term = int(search_term)
        poke_data = Pokemon.objects.filter(Q(height__icontains=search_term)|Q(weight__icontains=search_term)|Q(number__icontains=search_term))
    else:
        poke_data = Pokemon.objects.filter(Q(name__icontains=search_term)|Q(types__icontains=search_term))
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
