from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
import django.contrib.auth
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import BlogPost


def index(request):
    blogposts = BlogPost.objects.filter(public='True').order_by('date_created')
    context = {
        blogposts: blogposts,
    }
    return render(request, 'blog_app/index.html', context)

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
    # assign variables
    title = request.POST['title']
    body = request.POST['body']
    # date created
    date_created = timezone.now()
    # verify whether it is public or not
    public = 'public' in request.POST
    # assigning the user
    user = django.contrib.auth.get_user(request)
    blogpost_set = BlogPost(title=title, body=body, date_created=date_created, public=public, user=user)
    blogpost_set.save()
    return render(request, 'blog_app/profile.html')