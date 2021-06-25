from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Contact
from django.db.models import Q
from django.core.paginator import Paginator
import json

def index(request):
    return render(request, 'contacts/index.html')

def contacts(request):

    # return JsonResponse({'name': 'bob', 'age': 45})
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

    contacts = Contact.objects.order_by('-id').filter(Q(name__icontains=search)|Q(email__icontains=search))
    # contacts = Contact.objects.filter(name__icontains=search, email__icontains=email)

    paginator = Paginator(contacts, limit)
    if page > paginator.num_pages:
        contacts = []
    else:
        contacts = paginator.page(page)

    contacts_data = []
    for contact in contacts:
        contacts_data.append({
            'id': contact.id,
            'name': contact.name,
            'email': contact.email,
            'favorited': contact.favorited,
            'tags': [tag.name for tag in contact.tags.all()]
        })
    return JsonResponse({'contacts': contacts_data, 'total_pages': paginator.num_pages})


def create(request):
    # print(request.body)
    # request.body is JSON
    # turn the JSON into a Python dictionary
    data = json.loads(request.body)
    # create a Contact from our data and save it to the database
    contact = Contact(name=data['name'], email=data['email'])
    contact.save()
    # it doesn't really matter what we respond with
    return HttpResponse('ok')


def delete(request):
    print(request.GET)
    id = request.GET['id']
    contact = Contact.objects.get(id=id)
    contact.delete()
    return HttpResponse('ok')

def toggle_favorite(request):
    id = request.GET['id']
    contact = Contact.objects.get(id=id)
    contact.favorited = not contact.favorited
    contact.save()
    return HttpResponse('ok')