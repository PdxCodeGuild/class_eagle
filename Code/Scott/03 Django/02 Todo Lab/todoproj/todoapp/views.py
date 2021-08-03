from django.shortcuts import render
from .models import Priority, TodoItem

# Create your views here.
def index(request):
    todo_list = TodoItem.objects.order_by('-completed_date')
    context = {'todo_list': todo_list}
    return render(request, 'todoapp/index.html', context)

def submit(request):
    todo_item = TodoItem()
    priority = Priority()
    
    todo_item.text = request.POST['textInput']

    priority.name = request.POST['priorityInput']
    todo_item.priority = priority

    priority.save()
    todo_item.save()
    
    print(request.POST)
    context = {'todo_item': todo_item}
    return render(request, 'todoapp/submit.html', context) 
#TODO: fix this view