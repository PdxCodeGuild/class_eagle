from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import TodoItem, Priority

def index(request):
    priority = Priority.objects.all()
    todotasks = TodoItem.objects.all()
    context = {
        'priority' : priority,
        'todotask': todotasks,
    }
    return render(request, 'ToDo/index.html', context)


def add(request):
    task = request.POST['addtask']
    priority = request.POST['addpriority']
    todotasks_add = TodoItem(task=task, priority=priority)
    todotasks_add.save()
    return HttpResponseRedirect(reverse('ToDo:index'))