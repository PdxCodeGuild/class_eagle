from django.urls import path
from . import views

app_name = 'cipher_app'
urlpatterns = [
    path('', views.index, name='index')
]