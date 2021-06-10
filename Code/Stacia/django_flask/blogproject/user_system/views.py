from django.shortcuts import render, reverse
from django.contrib.auth.models import User
import django.contrib.auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages

# Create your views here.

def register(request):
    print(request.POST)
    if request.method == 'POST':
        form = User(request.Post) 
        form.save()
        username = request.POST['username']
        
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
            messages.success(request, f" Account created for {username}!")
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


def create(request):
    # check that we received form data
    print(request.POST)
    # get the values out of the form data
    username  = request.POST['user_name']
    
    password  = request.POST['password']
      # create a record and save it to the database
    user = User(user_name=user_name, password=password,)
    user.save()
    return HttpResponse ("home")

# def index(request):

#     return HttpResponse ("index")

# user = User.objects.create_user(
#             username, request.POST['email'], password)
#         user.first_name = request.POST['first_name']
#         user.last_name = request.POST['last_name']
#         user.save()


# def index(request):
#     if request.method =='POST':
#         form = RegForm(request.POST)
#         if form.is_valid():
#             # email = form.cleaned_data['contact_name']
#             # username = form.cleaned_data['contact_age']
#             # profile = Profile(email = email , username = username)
#             form.save()
#             form = RegForm()
#         else:
#             form = RegForm()
#         return render (request, "register/index.html", {"form": form})