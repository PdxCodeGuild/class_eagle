from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect
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


def delete(request, todo_item_id):
    todo_item = TodoItem.objects.get(id=todo_item_id)
    todo_item.delete()
    return HttpResponseRedirect(reverse('todoapp:index'))


def complete(request, todo_item_id):
    todo_item = TodoItem.objects.get(id=todo_item_id)
    completed_date_time = datetime.now()
    if todo_item.completed_date == None:
        todo_item.completed_date = completed_date_time
        todo_item.save()
    else:
        todo_item.completed_date = None
        todo_item.save()
    return HttpResponseRedirect(reverse('todoapp:index'))
