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
      
    priority_string = request.POST['priority']
    priority = Priority.objects.get(name=priority_string)
    created= timezone.now()
       # create a record and save it to the database
    todo_element = Todo(task=task, priority=priority,created=created)
    todo_element.save()

    
    # redirect to the index page
    return HttpResponseRedirect('/')
    
    # return HttpResponseRedirect(reverse('todoapp:index'))

def done(request, todo_id):
 todo_element = TodoItem.objects.get (id=todoitem_id)
 print(request.POST)
    # get the values out of the form data
    task = request.POST['task']
      
    priority_string = request.POST['priority']
    priority = Priority.objects.get(name=priority_string)
    created= timezone.now()
       # create a record and save it to the database
    done_todo = Done(task=task, priority=priority,created=created)
    done_todo.save()
    todo_element.delete()
    # redirect to the index page
    return HttpResponseRedirect('/')
    
    # return HttpResponseRedirect(reverse('todoapp:index'))

