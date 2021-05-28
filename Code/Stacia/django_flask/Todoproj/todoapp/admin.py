from django.contrib import admin

# Register your models here.
from.models import Todo,Priority
admin.site.register(Todo)
admin.site.register(Priority)