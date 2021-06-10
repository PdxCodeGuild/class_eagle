from django.shortcuts import get_object_or_404, render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
import django.contrib.auth
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import BlogPost, UserProfile
from .forms import EditForm


def index(request):
    blogposts = BlogPost.objects.filter(public='True').order_by('-date_created')
    context = {
        'blogposts': blogposts,
    }
    return render(request, 'blog_app/index.html', context)

def register(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        profile_image = request.POST['profile_picture']
        created_user = User.objects.create_user(username, email, password)
        bio = request.POST['bio']
        userprofile = UserProfile(user=created_user, profile_image=profile_image, bio=bio)
        userprofile.save()
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

def public(request, blogpost_user):
    blogposts = BlogPost.objects.filter(user_id=blogpost_user,public=True).order_by('-date_created')
    user = User.objects.get(id=blogpost_user)
    print(user)
    context = {
        'blogposts':blogposts,
        'user': user,
    }
    return render(request, 'blog_app/public.html', context)


@login_required
def profile(request):
    blogposts = request.user.blogpost.all().order_by('-date_created')
    user_profile = request.user.userprofile
    context = {
        'blogposts': blogposts,
        'user_profile': user_profile,
    }
    return render(request, 'blog_app/profile.html', context)

@login_required
def logout(request):
    django.contrib.auth.logout(request)
    return HttpResponseRedirect(reverse('blog_app:login'))

@login_required
def create(request):
    # assign variables
    title = request.POST['title']
    body = request.POST['body']
    # date created
    date_created = timezone.now()
    # verify whether it is public or not
    public = 'public' in request.POST
    # assigning the user
    user = django.contrib.auth.get_user(request)
    blogpost = BlogPost(title=title, body=body, date_created=date_created, public=public, user=user)
    blogpost.save()
    return HttpResponseRedirect(reverse('blog_app:profile'))

@login_required
def edit(request, blogpost_id):
    blogpost = BlogPost.objects.get(id=blogpost_id)
    form = EditForm(instance=blogpost)
    context = {
        'blogpost': blogpost,
        'form': form
        }
    return render(request, 'blog_app/edit.html', context)

@login_required
def edit_save(request, blogpost_id):
    blogpost = BlogPost.objects.get(id=blogpost_id)
    form = EditForm(request.POST, instance=blogpost)
    if form.is_valid():
        blogpost = form.save(commit=False)
        blogpost.date_edited = timezone.now()
        blogpost.save()
    return HttpResponseRedirect(reverse('blog_app:profile'))

@login_required
def delete(request, blogpost_id):
    blogpost = BlogPost.objects.get(id=blogpost_id)
    blogpost.delete()
    return HttpResponseRedirect(reverse('blog_app:profile'))