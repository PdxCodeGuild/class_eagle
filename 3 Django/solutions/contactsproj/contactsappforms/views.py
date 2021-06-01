from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import ContactForm

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
