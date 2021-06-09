
from django.urls import path
from . import views

app_name = 'blogapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:blog_post_id>/', views.detail, name='detail'),
]


