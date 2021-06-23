from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Contact
from django.db.models import Q
from django.core.paginator import Paginator

def index(request):
    return render(request, 'contacts/index.html')

def contacts(request):
    # JSON can only contain the following types:
    # Arrays, objects, null, boolean, number, string
    # Object of type QuerySet is not JSON serializable
    # contacts = Contact.objects.all()
    # return JsonResponse({'contacts': contacts})

    print(request.GET)

    search = request.GET.get('search', '')
    page = request.GET.get('page', '1')
    page = int(page) if page.isdigit() else 1
    # if page.isdigit():
    #     page = int(page)
    # else:
    #     page = 1
    limit = request.GET.get('limit', '10')
    limit = int(limit) if limit.isdigit() else 10

    contacts = Contact.objects.filter(Q(name__icontains=search)|Q(email__icontains=search))

    paginator = Paginator(contacts, limit)
    if page > paginator.num_pages:
        contacts = []
    else:
        contacts = paginator.page(page)

    contacts_data = []
    for contact in contacts:
        contacts_data.append({
            'name': contact.name,
            'email': contact.email
        })
    return JsonResponse({'contacts': contacts_data, 'total_pages': paginator.num_pages})
