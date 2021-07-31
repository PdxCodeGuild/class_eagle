from django.shortcuts import render
from .models import Priority, TodoItem

# Create your views here.
def index(request):
    todo_list = TodoItem.objects().order_buy('-completed_date')
    context = {'todo_list': todo_list}
    return render(request, 'todoapp/index.html', context)

def submit(request):
    todo_item = TodoItem()
    todo_item.text = request.POST['textInput']
#TODO: fix this view