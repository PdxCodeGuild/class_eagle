
from django.urls import path 
from . import views

app_name = 'blogapp'
urlpatterns = [
   
    # path('index', views.index, name = 'index'),
 
    path('splash/', views.splash, name='splash'),
    path ('home',views.home, name ="home"),
]