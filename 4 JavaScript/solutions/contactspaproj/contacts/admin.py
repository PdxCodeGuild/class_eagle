from django.contrib import admin

from .models import Contact, Tag

admin.site.register(Contact)
admin.site.register(Tag)