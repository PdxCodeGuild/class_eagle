from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    birthday = models.DateField()
    organ_donor = models.BooleanField()

    def __str__(self):
        return self.name + ' (' + self.email + ')'


