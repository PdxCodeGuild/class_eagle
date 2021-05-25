from django.shortcuts import render
from django.http import HttpResponse
from .models import Priority, TodoItem
from datetime import datetime


def index(request):
    todo_items = TodoItem.objects.all()
    context = {
        'title': 'Todo List',
        'todo_items': todo_items,
    }
    return render(request, 'todoapp/index.html', context)


def save_todo_item():
    ...
