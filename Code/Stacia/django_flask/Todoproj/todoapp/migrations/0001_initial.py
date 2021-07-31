# Generated by Django 3.2.3 on 2021-07-29 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('deadline', models.DateField(auto_now_add=True)),
                ('done', models.BooleanField()),
                ('priority', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='todoapp.priority')),
            ],
        ),
    ]
