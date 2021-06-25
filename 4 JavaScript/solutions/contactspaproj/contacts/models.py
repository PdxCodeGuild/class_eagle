from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=200)

    # https://stackoverflow.com/questions/46360477/attributeerror-nonetype-object-has-no-attribute-attname-django
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    favorited = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name='contacts')

    def __str__(self):
        return self.name + ' (' + self.email + ')'





