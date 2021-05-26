
from django.urls import path
from . import views

app_name = 'shortenerapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('shorten/', views.shorten, name='shorten'),
    path('<str:code>/', views.redirect, name='redirect'),
]



