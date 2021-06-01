from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Priority, Todo
from datetime import datetime



        
def index(request):
    todos = Todo.objects.all()
    
    
  
    context = {
        
        "todos":todos
    }
    return render(request, 'todoapp/index.html', context)


def create(request):
    # check that we received form data
    print(request.POST)
    # get the values out of the form data
    task = request.POST['task']
    time = request.post[]
   
    priority_string = request.POST['priority']
    priority = Priority.objects.get(name=priority_string)
   

    # create a record and save it to the database
    todo = Todo(task=task, priority=priority,)

    

    todo.save()
    # redirect to the index page
    return HttpResponseRedirect('/')
    
    # return HttpResponseRedirect(reverse('todoapp:index'))