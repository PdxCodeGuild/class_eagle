from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem, Priority
from datetime import datetime
from django.utils import timezone
import requests









def index(request):
    url = 'https://inspiration.goprogram.co.uk'
    response = requests.get(url)
    data = response.json()
    quote = data['quote']
    author = data['author']
    todo_items = TodoItem.objects.order_by('-priority')
    priorities = Priority.objects.all()
    context = {
        'title': 'Todo List',
        'todo_items': todo_items,
        'priorities' : priorities,
        'quote': quote,
        'author': author,
    }
    
    return render(request, 'todo_app/index.html', context)


def create(request):
    print(request.POST)
    # saving the data recieved to variables
    title = request.POST['title']
    priority = request.POST['priority_id']
    due_date = request.POST['due_date']
    detail = request.POST['detail']
    due_time = request.POST['due_time']
    due_date = datetime.strptime(due_date, '%b %d, %Y') # using strptime to get the date in the format needed
    created_date = timezone.now()
    # created_date = datetime.strptime(created_date, '%b %d, %Y') # using strptime to get the date in the format needed
    # sending and saving the information to the database
    todoitem_set = TodoItem(title=title, priority_id=priority, due_date=due_date, due_time=due_time, created_date=created_date, detail=detail)
    todoitem_set.save()
    # trying out the reverse lookup  option
    return HttpResponseRedirect(reverse('todo_app:index'))

def delete(request, todoitem_id):
    todoitem_set = TodoItem.objects.get(id=todoitem_id)
    todoitem_set.delete()
    return HttpResponseRedirect(reverse('todo_app:index'))