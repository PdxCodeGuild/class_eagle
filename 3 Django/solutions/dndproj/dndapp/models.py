from django.db import models



class DamageType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class InventoryItemType(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name



class Species(models.Model):
    name = models.CharField(max_length=200)
    vulnerabilities = models.ManyToManyField(DamageType, related_name='monsters_vulnerable')
    resistances = models.ManyToManyField(DamageType, related_name='monsters_resistant')

    def __str__(self):
        return self.name


class Monster(models.Model):
    name = models.CharField(max_length=200)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    inventory = models.ManyToManyField(InventoryItemType)

    def __str__(self):
        return self.name + ' (' + self.species.name + ')'

class MonsterInventoryItem(models.Model):
    inventory_item = models.ForeignKey(InventoryItemType, on_delete=models.CASCADE)
    monster = models.ForeignKey(Monster, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.monster.name + ' has ' + str(self.quantity) + ' ' + self.inventory_item.name
