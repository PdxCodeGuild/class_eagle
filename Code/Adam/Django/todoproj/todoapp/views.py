from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Priority, TodoItem
from datetime import datetime



def index(request):
    todo_items = TodoItem.objects.all()
    priorities = Priority.objects.all()
    context = {
        'title': 'Todo List',
        'todo_items': todo_items,
        'priorities': priorities,
    }
    return render(request, 'todoapp/index.html', context)


def create(request):
    print(request.POST)
    new_task = request.POST['new_task']
    priority = request.POST['priority']
    priority = int(priority)
    priority = get_object_or_404(Priority, id=priority)
    todo_item = TodoItem(text=new_task, priority=priority)
    todo_item.save()
    return HttpResponseRedirect(reverse('todoapp:index'))