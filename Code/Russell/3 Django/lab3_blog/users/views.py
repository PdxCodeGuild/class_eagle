from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import django.contrib.auth
from django.contrib.auth import logout,login,authenticate
from blog.models import Blogpost

def register(request):
    print(request.POST)
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        existing_user = User.objects.filter(username=username)
        if existing_user is not None:
            render(request, 'users/register.html', { 'error': 'A user with that name already exists.'})
            user = User.objects.create_user(username, email, password)
            django.contrib.auth.login(request, user)
        return HttpResponseRedirect(reverse('users:profile'))
            
    return render(request, 'users/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = django.contrib.auth.authenticate(request, username=username, password=password)
        if user is not None:
            print(username)
            django.contrib.auth.login(request, user)
            return HttpResponseRedirect(reverse('blog:blog-home'))
        else:
            return render(request, 'users/login.html', {'error': 'Bad username / password'})
    return render(request, 'users/login.html')

@login_required
def profile(request):
    logged_in_user = request.user.username
    print(logged_in_user)
    user_posts = Blogpost.objects.filter(user=request.user)
    context = {
        'user_posts': user_posts
    }
    print(context)
    return render(request, 'users/profile.html', context)
    
def logout(request):
    django.contrib.auth.logout(request)
    return HttpResponseRedirect(reverse('users:login')) 



