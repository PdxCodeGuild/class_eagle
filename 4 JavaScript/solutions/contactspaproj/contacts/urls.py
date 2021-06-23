
from django.urls import path
from . import views

app_name = 'contacts'
urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.contacts, name='contacts'),
    path('create/', views.create, name='create'),
    path('delete/', views.delete, name='delete'),
]

