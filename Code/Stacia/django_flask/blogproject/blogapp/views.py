from django.shortcuts import render, reverse
from django.utils import timezone
import django.contrib.auth
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post


def index(request):
    post = Post.objects.filter(public='True').order_by('-date_created')
    context = {
        'posts': posts,
    }
    return render(request, 'blog_app/index.html', context)

def splash(request):
    # print(request.POST)
    context ={
        'posts': Post.objects.all()
    }
    
    if request.method == 'POST':
        print(request.POST)
    # rant = request.POST['rant']
    return render(request, 'blogapp/splash.html', context)



def home (request):
    context ={
        'posts': Post.objects.all()
    }   
    
    return render(request, 'blogapp/home.html', context)


def create(request):
    # assign variables
    title = request.POST['title']
    rant = request.POST['rant']
   
    
    # assigning the user
    user = django.contrib.auth.get_user(request)
    post = Post(title=title, rant=rant,  author=user)
    post.save()\

    print(post)
    return HttpResponseRedirect(reverse('blogapp:splash'))