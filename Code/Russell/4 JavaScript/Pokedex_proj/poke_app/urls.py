from django.urls import path
from . import views

app_name = 'poke_app'
urlpatterns = [
    path ('index/', views.index, name='index'),
    path ('pokemon/', views.pokemon, name='pokemon')
]