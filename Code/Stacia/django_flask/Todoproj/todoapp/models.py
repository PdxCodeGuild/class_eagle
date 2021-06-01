from django.db import models
import datetime
from django.utils import timezone


class Priority(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Todo(models.Model):
    task = models.CharField(max_length=20)
    priority = models.ForeignKey(Priority,on_delete=models.PROTECT, null=True, blank=True)
    time = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return self.task

        