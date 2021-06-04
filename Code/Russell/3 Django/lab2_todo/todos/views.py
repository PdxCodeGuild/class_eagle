from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Priority, TodoItem

def index(request):
    todo_items = TodoItem.objects.all()
   
    context = {
        'todo_items':todo_items
        
    }

    print(context)

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


    

 

   


