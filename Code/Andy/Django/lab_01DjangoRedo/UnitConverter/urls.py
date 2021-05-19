from django.urls import path
from . import views

app_name = 'UnitConverter'
urlpatterns = [
    path('', views.index, name='index')
]