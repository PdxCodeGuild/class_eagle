from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
import django.contrib.auth
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'blog_app/index.html')

def register(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)
        return HttpResponseRedirect(reverse('blog_app:index'))
    return render(request, 'blog_app/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = django.contrib.auth.authenticate(request, username=username, password=password)
        if user is not None:
            django.contrib.auth.login(request,user)
            return HttpResponseRedirect(reverse('blog_app:index'))
        else:
            return render(request, 'blog_app/login.html', {'error': 'Incorrect username or password'})
    else:
        return render(request, 'blog_app/login.html')


@login_required
def profile(request):
    return render(request, 'blog_app/profile.html')

def logout(request):
    django.contrib.auth.logout(request)
    return HttpResponseRedirect(reverse('blog_app:login'))

def create(request):
    print(request.POST)
    return render(request, 'blog_app/profile.html')