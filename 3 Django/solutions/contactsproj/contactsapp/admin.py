from django.contrib import admin

from .models import Contact, City

admin.site.site_header = 'Contacts Admin'


admin.site.register(Contact)
admin.site.register(City)
