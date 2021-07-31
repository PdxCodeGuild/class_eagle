from django.shortcuts import render, reverse
from django.contrib.auth.models import User
import django.contrib.auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages

# Create your views here.

def register(request):
    print(request.POST)
    # get post and asign dictionary keys from form.
    if request.method == 'POST':
        # if form.is_valid(): 
        # form = User(request.POST)
        username = request.POST['username']
        email = request.POST ['email']
        password = request.POST['password']
        existing_user = User.objects.filter(username=username).first()

        # check if user exists
        if existing_user is not None:
            return render(request, 'user_system/register.html', {'error': 'That username is already taken'})
        user = User.objects.create_user(username, email, password)
        django.contrib.auth.login(request, user)
         
        # form.save()
        return HttpResponseRedirect(reverse('blogapp:splash'))
    return render(request, 'user_system/register.html')


def base(request):
    return render(request, "user_system/base.html")
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = django.contrib.auth.authenticate(request, username=username, password=password)
        if user is not None:
            django.contrib.auth.login(request, user)
            messages.success(request, f" hi {username}!")
            return HttpResponseRedirect(reverse('blogapp:splash'))
        else:
            return render(request, 'user_system/login.html', {'error': 'Bad news, thats not your user name, Good NEWS! That username is avalible!'})
    return render(request, 'user_system/login.html')
     
@login_required
def profile(request):
    print(request.user.username)
    return render(request, 'user_system/profile.html')

def logout(request):
    django.contrib.auth.logout(request)
    return HttpResponseRedirect(reverse('user_system:login'))



def create(request):
    # check that we received form data
    print(request.POST)
    # get the values out of the form data
    
      # create a record and save it to the database
    user = User(user_name=user_name, password=password,)
    user.save()
    return HttpResponse ("home")


