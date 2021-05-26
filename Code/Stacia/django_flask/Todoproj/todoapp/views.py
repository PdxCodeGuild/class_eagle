from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Todo
from datetime import datetime



        
def index(request):
    todo = Todo.objects.all()
    
    print(task)
  
    context = {
        
        'task': task,
        'priority': priority,
        'time': time,
    }
    return render(request, 'todoapp/index.html', context)


def create(request):
    # check that we received form data
    print(request.POST)
    # get the values out of the form data
    todo = request.POST['todo']
    
    priority = request.POST['priority']
    time = datetime.strptime(time, '%b %d, %Y')
    
   
    # create a record and save it to the database
    todo = Task(task=task, priority=priority, time=time,)

    

    todo.save()
    # redirect to the index page
    # return HttpResponseRedirect('/')
    # return HttpResponseRedirect('https://wwww.google.com/')
    return HttpResponseRedirect(reverse('todoapp:index'))