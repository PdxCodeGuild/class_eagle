from django.urls import path 
from . import views

app_name = "todoapp"
urlpatterns = [
     path('', views.index, name='index'),
     path('create/',views.create, name="create"),
     path('done/<int:todo_id>',views.done, name="done")
]