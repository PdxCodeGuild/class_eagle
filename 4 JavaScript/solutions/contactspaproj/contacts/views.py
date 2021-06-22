from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Contact


def index(request):
    return render(request, 'contacts/index.html')

def contacts(request):
    # JSON can only contain the following types:
    # Arrays, objects, null, boolean, number, string
    # Object of type QuerySet is not JSON serializable
    # contacts = Contact.objects.all()
    # return JsonResponse({'contacts': contacts})

    contacts = Contact.objects.all()
    contacts_data = []
    for contact in contacts:
        contacts_data.append({
            'name': contact.name,
            'email': contact.email
        })
    return JsonResponse({'contacts': contacts_data})
