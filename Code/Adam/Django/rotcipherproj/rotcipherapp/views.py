from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'title': 'ROT Cipher'
    }
    return render(request, 'rotcipherapp/index.html', context)
