# Generated by Django 3.2.3 on 2021-06-25 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_contact_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='tags',
        ),
    ]
