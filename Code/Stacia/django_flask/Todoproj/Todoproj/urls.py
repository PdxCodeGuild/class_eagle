
from django.urls import path, include
from django.contrib import admin
app_name = 'todoapp'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todoapp.urls')),
]

