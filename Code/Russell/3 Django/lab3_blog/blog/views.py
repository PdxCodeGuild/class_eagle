from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

posts = [
    {
        'author': 'russell',
        'title': 'posty-post',
        'content': 'Life ain\'t always so heck.',
        'date_created': 'Jan 12 2020',
    },
      {
        'author': 'Satan',
        'title': 'I want your soul',
        'content': 'I can has soul?',
        'date_created': 'Jan 13 2020',
    }
]

def index(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context)

def create(request):
    return render(request, 'blog/create.html')



