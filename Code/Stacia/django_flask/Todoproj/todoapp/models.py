from django.db import models
import datetime
from django.utils import timezone




class Todo(models.Model):
    name = models.CharField(max_length=200)
    priority = models.CharField(max_length=200, default="Low")
    deadline = models.DateField(auto_now_add=True)
    ogday = datetime.date.today()
    done = models.BooleanField()
    

    def __str__(self):
        return self.name
