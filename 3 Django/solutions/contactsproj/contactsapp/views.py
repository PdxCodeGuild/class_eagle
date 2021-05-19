from django.shortcuts import render
# from django.http import HttpResponse


def index(request):
    name = 'Joe'
    context = {
        'name': name,
        'title': 'Contacts'
    }
    return render(request, 'contactsapp/index.html', context)

