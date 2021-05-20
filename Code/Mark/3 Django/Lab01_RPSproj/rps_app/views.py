from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'title':'Rock Paper Scissors'
    }
    return render(request, 'rps_app/index.html', context) 