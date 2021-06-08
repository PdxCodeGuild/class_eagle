from django.shortcuts import render, reverse
from django.contrib.auth.models import User
import django.contrib.auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from blog.models import Blogpost

def register(request):
    print(request.POST)
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)
        django.contrib.auth.login(request, user)
        return HttpResponseRedirect(reverse('users:profile'))

    return render(request, 'users/register.html')

@login_required
def profile(request):
    logged_in_user = request.user
    logged_in_user_posts = Blogpost.objects.filter(user=logged_in_user)
    print(logged_in_user_posts)
    context = {
        'posts': logged_in_user_posts
    }
    return render(request, 'users/profile.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = django.contrib.auth.authenticate(request, username=username, password=password)
        if user is not None:
            django.contrib.auth.login(request, user)
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            return render(request, 'users/login.html', { 'error': 'Invalid username / password' })
    return render(request, 'users/login.html')

def logout(request):
    django.contrib.auth.logout(request)
    return HttpResponseRedirect(reverse('users:login'))