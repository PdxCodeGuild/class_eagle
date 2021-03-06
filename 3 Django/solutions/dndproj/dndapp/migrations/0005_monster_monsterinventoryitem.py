# Generated by Django 3.2.3 on 2021-06-30 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dndapp', '0004_auto_20210630_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dndapp.species')),
            ],
        ),
        migrations.CreateModel(
            name='MonsterInventoryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('inventory_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dndapp.inventoryitemtype')),
                ('monster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dndapp.monster')),
            ],
        ),
    ]
