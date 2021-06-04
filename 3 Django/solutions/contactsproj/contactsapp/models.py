from django.db import models
from django.contrib.auth.models import User



# >>> from contactsapp.models import Contact, City
# >>> from django.contrib.auth.models import User
# >>> contact = Contact.objects.get(id=1)
# >>> contact.name
# 'Wendy Carson'
# >>> contact.city.name
# 'Portland'
# >>> city = City.objects.get(id=1)
# >>> city.name
# 'Portland'
# >>> city.contact_set.all()
# <QuerySet [<Contact: user1 - Wendy Carson (1 Portland)>, <Contact: admin - 
# Brian Barber (1 Portland)>]>
# >>> contact.name
# 'Wendy Carson'
# >>> contact.user.username
# 'user1'
# >>> user = User.objects.get(id=1)
# >>> user.username
# 'admin'
# >>> user.contacts.all()
# <QuerySet [<Contact: admin - Brian Barber (1 Portland)>, <Contact: admin - 
# Jean R. Chatfield (3 Salem)>, <Contact: admin - Pat A. Marks (2 Eugene)>]> 


class City(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    birthday = models.DateField()
    organ_donor = models.BooleanField()
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')

    def __str__(self):
        return self.user.username + ' - ' + self.name + ' (' + str(self.city_id) + ' ' + self.city.name + ')'


