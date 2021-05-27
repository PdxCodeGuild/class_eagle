from django.urls import path
from . import views

app_name = 'todoapp'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('delete/<int:todo_item_id>/', views.delete, name='delete'),
    path('complete/<int:todo_item_id>/', views.complete, name='complete'),
]