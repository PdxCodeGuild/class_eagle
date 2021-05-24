from django.urls import path
from . import views

app_name = 'unitconverterapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('', views.result, name='result')
]