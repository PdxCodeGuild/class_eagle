
from django.urls import path
from . import views

app_name = 'contactsappforms'
urlpatterns = [
    path('create/', views.create, name='create'),
    path('edit/<int:contact_id>/', views.edit, name='edit'),
    path('edit/<int:contact_id>/save/', views.edit_save, name='edit_save')
]

