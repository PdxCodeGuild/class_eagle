# Generated by Django 3.2.3 on 2021-06-24 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='favorited',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
