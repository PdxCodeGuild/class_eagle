# Generated by Django 3.2.3 on 2021-06-07 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_rename_autho_post_author'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User_Info',
        ),
    ]