


from django.urls import path
from . import views

app_name = 'pokedexapp'
urlpatterns = [
    path('pokedex/', views.pokedex, name='pokedex')
]