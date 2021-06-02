from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from contactsapp.models import Contact

@login_required
def create(request):
    if request.method == 'POST':
        # print(request.POST)
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
    form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'contactsappforms/create.html', context)


@login_required
def edit(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    form = ContactForm(instance=contact)
    context = {
        'form': form,
        'contact': contact
    }
    return render(request, 'contactsappforms/edit.html', context)

@login_required
def edit_save(request, contact_id):
    # print(request.POST)
    contact = Contact.objects.get(id=contact_id)
    form = ContactForm(request.POST, instance=contact)
    if form.is_valid():
        contact = form.save()
    return HttpResponseRedirect(reverse('contactsappforms:edit', args=(contact.id,)))