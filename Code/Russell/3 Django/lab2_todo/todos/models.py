from django.db import models
from django.utils import timezone
import datetime

class Priority(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class TodoItem(models.Model):
    text = models.CharField(max_length=200)
    priority = models.ForeignKey(Priority, on_delete=models.PROTECT)
    created_date = models.DateTimeField()

    def __str__(self):
        return self.text
