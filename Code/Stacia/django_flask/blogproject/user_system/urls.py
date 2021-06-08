from django.urls import path 
from . import views

app_name = 'user_system'
urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/', views.login,name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('create/', views.create, name='create'),
    # path('index', views.index, name = 'index'),
]