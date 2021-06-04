from django.shortcuts import render
from .models import Blogpost


def index(request):
    all_posts = Blogpost.objects.all()
    context = {
        'all_posts': all_posts,
    }
    print(all_posts)
    return render(request, 'blog/index.html', context)
