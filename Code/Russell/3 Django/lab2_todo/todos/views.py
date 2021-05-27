from django.shortcuts import render
from django.http import HttpResponse
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
    print(item, priority)
    return HttpResponse('ok')

 

   


