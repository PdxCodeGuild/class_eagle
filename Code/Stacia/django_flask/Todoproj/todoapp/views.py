from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.db import models
from datetime import datetime
from .models import Todo






        
def index(request):
    todos = Todo.objects.all()
    

    context = {
        
        "todos":todos,
    }
    return render(request, 'todoapp/index.html', context)


def create(request):

    # if request.method =='POST':
    # check that we received form data
    # print(request.POST)
    print(request.POST)
    # get the values out of the form data

    name = request.POST.get('todo')
    priority= request.POST.get('priority')
    
    
    done= False

        # # create a record and save it to the database
    todo = Todo.objects.create(name=name, priority=priority,done = done)
    todo.save()

    # redirect to the index page
    
    return HttpResponseRedirect(reverse('todoapp:index'))

def done(request, todo_id):
    print(request.POST)
    # # print(todo_element)
    # # get the values out of the form data
    todo = Todo.objects.get(id=todo_id)
    # task = request.POST['todo']
    # console.log(task)
    # print(task.name)
    # priority_string = request.POST['priority']
    # priority = Priority.objects.get(name=priority_string)
    todo.done =True
    # todo = todo()
    # todo.name= name 
    # todo.priority = priority
    # todo.save = true
    todo.save()
    # print (todo)
    
    # create a record and save it to the database
    # done_todo = Done(task=task, priority=priority,created=created)
    # done_todo.save()
    # todo_element.delete()
    # redirect to the index page
 
    return HttpResponseRedirect(reverse('todoapp:index'))


