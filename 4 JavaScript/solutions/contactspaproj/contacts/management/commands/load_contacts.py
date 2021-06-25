from django.core.management.base import BaseCommand
import json
from contacts.models import Contact, Tag

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

            contact = Contact(name=name, email=email, favorited=False)
            contact.save()

            for tag_name in contact_data['tags']:
                # tag = Tag.objects.get(name=tag_name)
                tag, created = Tag.objects.get_or_create(name=tag_name)
                contact.tags.add(tag)
                # tag.contacts.add(contact)

            


            