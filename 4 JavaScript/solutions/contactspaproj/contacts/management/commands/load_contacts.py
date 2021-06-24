from django.core.management.base import BaseCommand
import json
from contacts.models import Contact

class Command(BaseCommand):

    def handle(self, *args, **options):
        Contact.objects.all().delete()
        with open('contacts/management/commands/contacts.json') as file:
            text = file.read()
        # turn raw JSON into a dictionary
        data = json.loads(text) # dictionary containing a list of dictionaries
        contacts_data = data['contacts'] # list of dictionaries
        for contact_data in contacts_data:
            name = contact_data['name']
            email = contact_data['email']
            tags = ','.join(contact_data['tags'])
            print(tags)
            # save data to our database
            contact = Contact(name=name, email=email, favorited=False, tags=tags)
            contact.save()


            