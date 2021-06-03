from django.urls import path
from . import views

app_name = 'blog_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('create/', views.create, name='create'),
    path('edit/<int:blogpost_id>', views.edit, name='edit'),
    path('edit_save/<int:blogpost_id>', views.edit_save, name='edit_save'),
    path('delete/<int:blogpost_id>', views.delete, name='delete')
]  