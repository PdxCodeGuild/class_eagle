from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Blogpost
from django.utils import timezone



def index(request):
    context = {
        'posts': Blogpost.objects.all()
    }
    return render(request, 'blog/index.html', context)

def create(request):
    return render(request, 'blog/create.html')

def save(request):
    title = request.POST['title']
    post = request.POST['body']
    public = 'public' in request.POST
    blogpost = Blogpost(title=title, post=post, public=public, user=request.user)
    blogpost.save()
    print(request.POST)
    return HttpResponseRedirect(reverse('blog:blog-home'))






