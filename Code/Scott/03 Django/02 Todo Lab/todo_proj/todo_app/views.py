from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse

from .models import Priority, TodoItem
from .forms import TodoForm

from datetime import datetime

# Create your views here

def index(request):
    todo_items = TodoItem.objects.order_by('-created_date')
    form = TodoForm()

    context = {'todo_items': todo_items, 'form': form}
    return render(request, 'todo_app/index.html', context)

def save_todo_item(request):
    print(request.POST)

    text = request.POST['text']
    created_date = datetime.now()
    priority = request.POST['priority']

    todo_item = TodoItem(text=text, created_date=created_date, priority_id=priority)
    todo_item.save()

    return HttpResponseRedirect(reverse('todo_app:index'))