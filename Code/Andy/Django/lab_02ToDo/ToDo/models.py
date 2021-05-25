from typing import Text
from django.db import models
from django.utils import timezone
 

class Priority(models.Model):
    pri = models.CharField(max_length=100)

    def __str__(self):
        return self.pri


class TodoItem(models.Model):
    task = models.TextField(max_length=100)
    priority = models.ForeignKey(Priority,null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.task