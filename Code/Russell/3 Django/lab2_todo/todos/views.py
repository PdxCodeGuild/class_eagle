from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'message': 'How you doin\' globe?'
    }
    return render(request, 'todos/index.html', context)

