from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import ShortURL
import random
import string

def index(request):
    urls = ShortURL.objects.all()
    context = {
        'urls': urls
    }
    return render(request, 'shortenerapp/index.html', context)

def shorten(request):
    print(request.POST)
    long_url = request.POST['long_url']
    print(long_url)
    code = ''
    for i in range(6):
        code += random.choice(string.ascii_letters + string.digits)
    print(code)
    short_url = ShortURL(code=code, url=long_url)
    short_url.save()
    return HttpResponseRedirect(reverse('shortenerapp:index'))


def redirect(request, code):
    # look up the ShortURL with the given code
    # url = ShortURL.objects.get(code=code)
    short_url = get_object_or_404(ShortURL, code=code)
    short_url.clicks += 1
    short_url.save()
    # redirect to the long url associated with it
    return HttpResponseRedirect(short_url.url)

