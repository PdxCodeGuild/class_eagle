# Generated by Django 3.2.3 on 2021-05-25 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0005_remove_todoitem_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='priority',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ToDo.priority'),
        ),
    ]
