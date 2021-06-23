from django.shortcuts import render
from .models import Pokemon


def pokedex(request):
    # all_pokemon = Pokemon.objects.all().order_by('number')
    return render(request, 'pokedexapp/pokedex.html')
