


from django.urls import path
from . import views

app_name = 'pokedexapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('pokemon/', views.pokemon, name='pokemon')
]