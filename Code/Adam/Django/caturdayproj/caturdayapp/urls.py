from django.urls import path
from . import views

app_name = 'caturdayapp'
urlpatterns = [
    path('', views.index, name='index')
]
