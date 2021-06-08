from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('entry/<int:post_id>/', views.entry, name='entry'),
]