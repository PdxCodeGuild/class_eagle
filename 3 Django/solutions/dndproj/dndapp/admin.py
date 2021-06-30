from django.contrib import admin

from .models import Species, DamageType, InventoryItemType, Monster, MonsterInventoryItem

admin.site.register(Species)
admin.site.register(DamageType)
admin.site.register(InventoryItemType)
admin.site.register(Monster)
admin.site.register(MonsterInventoryItem)