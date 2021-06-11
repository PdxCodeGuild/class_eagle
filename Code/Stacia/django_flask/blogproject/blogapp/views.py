from django.shortcuts import render, reverse
from django.utils import timezone
import django.contrib.auth
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post

def splash(request):
    # print(request.POST)
    if request.method == 'POST':
        print(request.POST)
    # rant = request.POST['rant']
    return render(request, 'blogapp/splash.html',)


def home (request):
    context ={
        'posts': Post.objects.all()

    }
    return render(request, 'blogapp/home.html', context)

