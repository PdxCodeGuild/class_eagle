from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import User
import django.contrib.auth

def register(request):
    # if we're receiving a form submission
    if request.method == 'POST':
        # get the form data out of request.POST
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        photo = request.FILES['photo']
        password = request.POST['password']
        retype_password = request.POST['retype_password']
        # if the passwords don't match, render the template with an error message
        if password != retype_password:
            return render(request, 'users/register.html', {'error': 'the passwords you entered do not match'})
        # if a user with that username already exists, render the template with an error message
        if User.objects.filter(username=username).exists():
            return render(request, 'users/register.html', {'error': 'a user already exists with that username'})
        # create the user
        user = User.objects.create_user(username, email, password)
        user.photo = photo
        user.phone = phone
        user.save()
        # log the user in (set a cookie)
        django.contrib.auth.login(request, user)
        # redirect to the blog home page
        return HttpResponseRedirect(reverse('blogapp:index'))

    return render(request, 'users/register.html')


def login(request):
    # if we're receiving a form submission
    if request.method == 'POST':
        # get the form data out
        username = request.POST['username']
        password = request.POST['password']
        # authenticate the user
        user = django.contrib.auth.authenticate(request, username=username, password=password)
        if user is None:
            # if the user was not found, render the template with an error message
            return render(request, 'users/login.html', {'error': 'no user exists with that username and password'})
        else:
            # if the user was found
            # log the user in
            # redirect to the blog index page
            django.contrib.auth.login(request, user)
            return HttpResponseRedirect(reverse('blogapp:index'))
    return render(request, 'users/login.html')

def logout(request):
    # log the user out
    django.contrib.auth.logout(request)
    # redirect to the login page
    return HttpResponseRedirect(reverse('users:login'))

