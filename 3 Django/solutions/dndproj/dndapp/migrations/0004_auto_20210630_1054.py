# Generated by Django 3.2.3 on 2021-06-30 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dndapp', '0003_rename_inventoryitem_inventoryitemtype'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Monster',
            new_name='Species',
        ),
        migrations.DeleteModel(
            name='MonsterInventoryItem',
        ),
    ]
