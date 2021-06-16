from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
import requests
import urllib.parse
from .models import DadJoke
from django.utils import timezone


def index_of_any(text, chars):
    r = 999
    for char in chars:
        index = text.find(char)
        if index != -1 and index < r:
            r = index
    if r == 999:
        return -1
    return r

def index(request):

    url = 'https://icanhazdadjoke.com/'
    response = requests.get(url, headers={'Accept': 'application/json'})
    data = response.json()
    joke = data['joke']
    # encoded_joke = urllib.parse.quote_plus(joke)

    # generate text for image macro
    sentences = joke.count('.') + joke.count('?') + joke.count('!') + joke.count(',')
    top_text = ''
    bottom_text = ''
    print(joke)
    print('sentences: ' + str(sentences))
    if sentences > 1:
        index = index_of_any(joke, ',.?!')
        print(index)
        top_text = joke[:index+1]
        bottom_text = joke[index+1:]
    else:
        top_text = '( ͡° ͜ʖ ͡°)'
        bottom_text = joke
    top_text = urllib.parse.quote_plus(top_text)
    bottom_text = urllib.parse.quote_plus(bottom_text)
    

    context = {
        'joke': joke,
        'top_text': top_text,
        'bottom_text': bottom_text
    }
    return render(request, 'dadjokeapp/index.html', context)



def save(request):
    joke = request.POST['joke']
    dad_joke = DadJoke(joke=joke, timestamp=timezone.now())
    dad_joke.save()
    return HttpResponseRedirect(reverse('dadjokeapp:favorites'))


def favorites(request):
    jokes = DadJoke.objects.order_by('-timestamp')
    context = {
        'jokes': jokes
    }
    return render(request, 'dadjokeapp/favorites.html', context)