from django.forms import ModelForm
from .models import TodoItem, Priority

class TodoForm(ModelForm):
    class Meta:
        model = TodoItem
        fields= ['text', 'priority']