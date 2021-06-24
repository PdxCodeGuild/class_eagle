from django.urls import path
from django.urls import path
from . import views

app_name = 'pokeappi'
urlpatterns = [
    path('pokeappi/', views.pokeappi, name='pokeappi')
    
]