from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Contact, City
from datetime import datetime
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    contacts = request.user.contacts.all()
    cities = City.objects.all()
    # print(contacts)
    # for contact in contacts:
    #     print(contact.name)
    # organ_donors = Contact.objects.filter(organ_donor=True)
    # alyssa = Contact.objects.get(id=2)
    context = {
        'title': 'Contacts',
        'contacts': contacts,
        'cities': cities
    }
    return render(request, 'contactsapp/index.html', context)

@login_required
def create(request):
    # check that we received form data
    print(request.POST)
    # get the values out of the form data
    name = request.POST['name']
    email = request.POST['email']
    birthday = request.POST['birthday']
    birthday = datetime.strptime(birthday, '%b %d, %Y')
    organ_donor = 'organ_donor' in request.POST # handle checkboxes in a special way
    city_id = request.POST['city_id']
    # create a record and save it to the database
    contact = Contact(name=name, email=email, birthday=birthday, organ_donor=organ_donor, city_id=city_id, user=request.user)

    # city = City.objects.get(id=city_id)
    # contact = Contact(name=name, email=email, birthday=birthday, organ_donor=organ_donor, city=city)

    contact.save()
    # redirect to the index page
    # return HttpResponseRedirect('/')
    # return HttpResponseRedirect('https://wwww.google.com/')
    return HttpResponseRedirect(reverse('contactsapp:index'))

def delete(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    contact.delete()
    return HttpResponseRedirect(reverse('contactsapp:index'))

def edit(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    cities = City.objects.all()
    context = {
        'contact': contact,
        'cities': cities
    }
    return render(request, 'contactsapp/edit.html', context)

def edit_save(request, contact_id):
    print(request.POST)
    contact = Contact.objects.get(id=contact_id)
    contact.name = request.POST['name']
    contact.email = request.POST['email']
    contact.birthday = datetime.strptime(request.POST['birthday'], '%b %d, %Y')
    contact.organ_donor = 'organ_donor' in request.POST # handle checkboxes in a special way
    contact.city_id = request.POST['city_id']
    contact.save()
    return HttpResponseRedirect(reverse('contactsapp:index'))