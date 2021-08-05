from django.urls import path
from . import views

app_name = 'pokeappi'
urlpatterns = [
    path('', views.index, name='index'),
    path('pokeappi/', views.pokeappi, name='pokeappi'),
   
]