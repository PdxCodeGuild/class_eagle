from django.db import models





class Todo(models.Model):
    task = models.CharField(max_length=200),
    time = models.DateField()
    
    
    

    def __str__(self):
        return self.task + '-' +self.time
