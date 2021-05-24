from django.db import models
from django.utils import timezone
 
class TodoItem(models.Model):
    task = models.TextField(max_length=100)

    def __str__(self):
        return self.task
 
class Priority(models.Model):
    priority = models.CharField(max_length=100)

    def __str__(self):
        return self.priority