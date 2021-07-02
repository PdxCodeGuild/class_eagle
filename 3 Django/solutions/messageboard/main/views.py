from django.shortcuts import render
import requests

from .models import Message
from .secrets import recaptcha_secret_key

def index(request):
    error_message = ''
    if request.method == 'POST':
        print(request.POST)

        recaptcha_response = request.POST['g-recaptcha-response']
        recaptcha_url = 'https://www.google.com/recaptcha/api/siteverify'
        response = requests.get(recaptcha_url, params={'response': recaptcha_response, 'secret': recaptcha_secret_key})
        print(response.text)
        if response.json()['success']:
            title = request.POST['title']
            author = request.POST['author']
            body = request.POST['body']
            message = Message(title=title, author=author, body=body)
            message.save()
        else:
            error_message = 'Bad recaptcha!'
    messages = Message.objects.order_by('-timestamp')
    context = {
        'messages': messages,
        'error_message': error_message
    }
    return render(request, 'main/index.html', context)
