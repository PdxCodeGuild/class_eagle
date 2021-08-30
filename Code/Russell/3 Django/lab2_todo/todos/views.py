from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Priority, TodoItem
from django.utils import timezone

def index(request):
    todo_items = TodoItem.objects.all()
   
    context = {
        'todo_items':todo_items
        
    }

    # print(context)

    return render(request, 'todos/index.html', context)

def update(request):
    print(request.POST)
    item = request.POST['item']
    priority = request.POST['priority']
    priority = Priority.objects.get(id = int(priority))
    todo = TodoItem()
    todo.text = item
    todo.priority = priority
    todo.save()
    print(item, priority)
    return HttpResponseRedirect(reverse('todos:index'))
    # return HttpResponse('ok')


def delete(request, todo_item_id):
    to_do_delete = TodoItem.objects.get(id= todo_item_id)
    to_do_delete.delete()
    return HttpResponseRedirect(reverse('todos:index'))


def done(request, todo_item_id):
    to_do_done = TodoItem.objects.get(id= todo_item_id)
    to_do_done.completed_date = timezone.now()
    to_do_done.save()
    # print(to_do_done.completed_date)
    print(to_do_done.completed_date)
    return HttpResponseRedirect(reverse('todos:index'))

    

 

   


