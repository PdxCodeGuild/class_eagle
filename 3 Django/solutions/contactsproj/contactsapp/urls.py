

from django.urls import path
from . import views

app_name = 'contactsapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    # localhost:8000/delete/5/
    path('delete/<int:contact_id>/', views.delete, name='delete')
]
