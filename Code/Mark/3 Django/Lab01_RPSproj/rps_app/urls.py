from django.urls import path
from . import views

app_name = 'rps_app'
urlpatterns = [
    path('', views.index, name='index')
] 