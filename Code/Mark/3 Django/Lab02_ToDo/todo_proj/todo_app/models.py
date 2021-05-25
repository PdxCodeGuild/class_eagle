from django.db import models

class Priority(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self):

        return self.name


class TodoItem(models.Model):
    title = models.CharField(max_length=20)
    priority = models.ForeignKey(Priority, on_delete=models.PROTECT)
    created_date = models.DateField()
    due_date = models.DateField(blank=True, null=True)

    def __str__(self):

        return self.title


