from django.urls import path
from . import views

app_name = 'roshamboapp'
urlpatterns = [
    path('index/', views.index, name='index')
]

