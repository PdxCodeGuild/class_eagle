from django.urls import path
from . import views

app_name = 'todos'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('update/', views.update, name='update'),
    path('<int:todo_item_id>', views.delete, name='delete'),
    path('<int:todo_item_id>/done/', views.done, name='done'),
    ]



