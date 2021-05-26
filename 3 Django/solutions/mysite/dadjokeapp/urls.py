
from django.urls import path
from . import views

app_name = 'dadjokeapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('save/', views.save, name='save'),
    path('favorites/', views.favorites, name='favorites'),
]