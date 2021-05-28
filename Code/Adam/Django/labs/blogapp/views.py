from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'title': 'Block Title',
        'content': 'Block Content',
    }
    return render(request, 'blogapp/index.html', context)

def register(request):
    return HttpResponse('Register here')

def login(request):
    return HttpResponse('Login here')

def profile(request):
    return HttpResponse('Profile here')