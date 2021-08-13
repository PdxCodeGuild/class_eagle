from django.urls import path
from . import views

app_name = 'blog'

urlpatterns =[
    path('', views.index, name='blog-home'),
    path('create/', views.create, name='create'),
    path('save/', views.save, name='save'),
]



