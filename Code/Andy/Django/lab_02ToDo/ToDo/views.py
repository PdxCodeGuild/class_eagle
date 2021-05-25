from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Priority, TodoItem 

def index(request):
    context = {
        'message': 'Hello World!'
    }
    return render(request, 'ToDo/index.html', context)
