from django.urls import path
from . import views

app_name = 'blog'

urlpatterns =[
    path('', views.index, name='blog-home'),
    path('create/', views.create, name='create'),
    path('save/', views.save, name='save'),
    path('edit/<int:edit_post_id>', views.edit, name='edit'),
    path('edit/<int:edit_post_id>/save', views.edit_save, name='edit_save'),
    path('delete/<int:edit_post_id>', views.delete, name='delete')
]



