from django.shortcuts import render, reverse
from django.utils import timezone
import django.contrib.auth
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post

def splash(request):

      return HttpResponse ("blogapp:splash")


def home (request):
    context ={
        'posts': Post.objects.all()

    }
    return render(request , 'blog/home.html' , context )

