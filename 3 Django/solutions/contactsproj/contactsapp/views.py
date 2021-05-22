from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Contact
from datetime import datetime

def index(request):
    contacts = Contact.objects.all()
    # print(contacts)
    # for contact in contacts:
    #     print(contact.name)
    # organ_donors = Contact.objects.filter(organ_donor=True)
    # alyssa = Contact.objects.get(id=2)
    context = {
        'title': 'Contacts',
        'contacts': contacts
    }
    return render(request, 'contactsapp/index.html', context)


def create(request):
    # check that we received form data
    print(request.POST)
    # get the values out of the form data
    name = request.POST['name']
    email = request.POST['email']
    birthday = request.POST['birthday']
    birthday = datetime.strptime(birthday, '%b %d, %Y')
    organ_donor = 'organ_donor' in request.POST # handle checkboxes in a special way
    # create a record and save it to the database
    contact = Contact(name=name, email=email, birthday=birthday, organ_donor=organ_donor)
    contact.save()
    # redirect to the index page
    # return HttpResponseRedirect('/')
    # return HttpResponseRedirect('https://wwww.google.com/')
    return HttpResponseRedirect(reverse('contactsapp:index'))

