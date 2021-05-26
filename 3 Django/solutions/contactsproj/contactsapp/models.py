from django.db import models



class City(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    birthday = models.DateField()
    organ_donor = models.BooleanField()
    city = models.ForeignKey(City, on_delete=models.PROTECT)

    def __str__(self):
        return self.name + ' (' + str(self.city_id) + ' ' + self.city.name + ')'


