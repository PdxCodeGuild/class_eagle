from django.contrib import admin

from .models import Contact

admin.site.site_header = 'Contacts Admin'


admin.site.register(Contact)

