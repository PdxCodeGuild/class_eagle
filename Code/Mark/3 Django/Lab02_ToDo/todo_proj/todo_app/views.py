from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem, Priority
from datetime import datetime
from django.utils import timezone

def index(request):
    todo_items = TodoItem.objects.order_by('priority')
    priorities = Priority.objects.all()
    context = {
        'title': 'Todo List',
        'todo_items': todo_items,
        'priorities' : priorities,
    }
    return render(request, 'todo_app/index.html', context)


def create(request):
    print(request.POST)
    # saving the data recieved to variables
    title = request.POST['title']
    priority = request.POST['priority_id']
    print(priority)
    due_date = request.POST['due_date']
    due_date = datetime.strptime(due_date, '%b %d, %Y') # using strptime to get the date in the format needed
    created_date = request.POST['created_date']
    created_date = datetime.strptime(created_date, '%b %d, %Y') # using strptime to get the date in the format needed
    # sending and saving the information to the database
    todoitem_set = TodoItem(title=title, priority_id=priority, due_date=due_date, created_date=created_date)
    todoitem_set.save()
    # trying out the reverse lookup  option
    return HttpResponseRedirect(reverse('todo_app:index'))