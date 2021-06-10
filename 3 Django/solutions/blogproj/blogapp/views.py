from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator

from .models import BlogPost

def index(request):
    blog_posts = BlogPost.objects.filter(public=True).order_by('-date_created')
    paginator = Paginator(blog_posts, 3)
    page = request.GET.get('page', 1)
    blog_posts_page = paginator.page(page)
    # first_post = blog_posts[0]
    # other_posts = blog_posts[1:]
    # context = {
    #     'first_post': first_post,
    #     'other_posts': other_posts
    # }
    context = {
        'blog_posts': blog_posts_page
    }
    return render(request, 'blogapp/index.html', context)

def detail(request, blog_post_id):
    # blog_post = BlogPost.objects.get(id=blog_post_id)
    blog_post = get_object_or_404(BlogPost, id=blog_post_id)
    context = {
        'blog_post': blog_post
    }
    return render(request, 'blogapp/detail.html', context)
