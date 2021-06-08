from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from .models import Blogpost
from datetime import datetime


def index(request):
    all_posts = Blogpost.objects.all()
    context = {
        'all_posts': all_posts,
    }
    print(all_posts)
    return render(request, 'blog/index.html', context)

@login_required
def create(request):
    print(request.POST)
    title = request.POST['title']
    body = request.POST['body']
    user_id = request.POST['user_id']
    public = 'public' in request.POST
    date_created = datetime.now()
    date_edited = None
    new_post = Blogpost(title=title, body=body, user_id=user_id, public=public, date_created=date_created, date_edited=date_edited )
    new_post.save()

    return HttpResponseRedirect(reverse('users:profile'))

def entry(request, post_id):
    blog_entry = Blogpost.objects.get(id=post_id)
    context = {
        'title': blog_entry.title,
        'author': blog_entry.user,
        'body': blog_entry.body,
        'date': blog_entry.date_created,
    }
    return render(request, 'blog/entry.html', context)

