

from django.urls import path
from . import views

app_name = 'contactsapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    # localhost:8000/delete/5/
    path('delete/<int:contact_id>/', views.delete, name='delete'),
    path('edit/<int:contact_id>/', views.edit, name='edit'),
    path('edit/<int:contact_id>/save/', views.edit_save, name='edit_save'),
]
