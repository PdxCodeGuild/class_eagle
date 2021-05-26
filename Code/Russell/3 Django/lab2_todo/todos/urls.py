from django.urls import path
from . import views

app_name = 'todos'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('update/', views.update, name='update'),
    ]



