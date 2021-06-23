from django.urls import path
from . import views

app_name = 'pokeapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('pokedex/', views.pokedex, name='pokedex')
]