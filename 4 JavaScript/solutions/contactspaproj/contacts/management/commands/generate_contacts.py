from django.core.management.base import BaseCommand
from contacts.models import Contact
from faker import Faker

class Command(BaseCommand):

    def handle(self, *args, **options):
        faker = Faker()
        # print(faker.name())
        # print(faker.email())
        for i in range(1000):
            contact = Contact(name=faker.name(), email=faker.email(), favorited=faker.boolean(), tags='')
            contact.save()
