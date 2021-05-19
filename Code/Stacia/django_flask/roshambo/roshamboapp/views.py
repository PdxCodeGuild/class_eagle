from django.shortcuts import render
from .models import BlogPost

def index(request):
    blog_posts = BlogPost.objects.order_by('-date_published')
    context = {
        'blog_posts': blog_posts
    }
    return render(request, 'roshamboapp/index.html', context)