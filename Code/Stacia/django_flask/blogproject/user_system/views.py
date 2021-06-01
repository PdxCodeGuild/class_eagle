from django.shortcuts import render, reverse
from django.contrib.auth.models import User
import django.contrib.auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


# Create your views here.
def register(request):
    print(request.POST)
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        existing_user = User.objects.filter(username=username).first()
        if existing_user is not None:
            return render(request, 'user_system/register.html', {'error': 'That username is already taken'})
        user = User.objects.create_user(username, email, password)
        django.contrib.auth.login(request, user)
        return HttpResponseRedirect(reverse('blogapp:index'))
    return render(request, 'user_system/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = django.contrib.auth.authenticate(request, username=username, password=password)
        if user is not None:
            django.contrib.auth.login(request, user)
            return HttpResponseRedirect(reverse('blogapp:index'))
        else:
            return render(request, 'user_system/login.html', {'error': 'thats not quite right try again!'})
    return render(request, 'user_system/login.html')
     
@login_required
def profile(request):
    print(request.user.username)
    return render(request, 'user_system/profile.html')

def logout(request):
    django.contrib.auth.logout(request)
    return HttpResponseRedirect(reverse('user_system:login'))