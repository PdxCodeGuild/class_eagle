from django.db import models


# Create your models here.
class Priority(models.Model):
    priorities = [('h', 'high'), ('m', 'medium'), ('l', 'low')]
    name = models.CharField(
        max_length=200,
        choices=priorities, 
    )

    def __str__(self):
        return self.name

class TodoItem(models.Model):
    priorities_dict = {'h': 'high', 'm': 'medium', 'l': 'low'}
    text = models.CharField(max_length=200)
    created_date = models.DateTimeField()
    priority = models.ForeignKey(
        Priority,
        null=True,
        on_delete=models.SET_NULL
    )
    
    def __str__(self):
        return f'Created: {self.created_date} | TODO: {self.text} | Priority: {self.priorities_dict[str(self.priority)]}'
