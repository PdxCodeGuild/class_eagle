from django.core.management.base import BaseCommand
from contacts.models import Contact
import string

class Command(BaseCommand):

    def handle(self, *args, **options):
        contacts = Contact.objects.all()
        for contact in contacts:
            name = contact.name
            for char in string.punctuation:
                name = name.replace(char, '')
            name = name.replace(' ', '')
            name = name.lower()
            contact.email = name + '@email.com'
            contact.save()

