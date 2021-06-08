from django.contrib import admin
from .models import BlogPost, UserProfile


admin.site.register(BlogPost)
admin.site.register(UserProfile)