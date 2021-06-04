from django.contrib import admin
from .models import Priority, TodoItem, Archive

admin.site.register(Priority)
admin.site.register(TodoItem)
admin.site.register(Archive)