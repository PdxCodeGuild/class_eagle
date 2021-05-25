# Generated by Django 3.2.3 on 2021-05-24 21:11

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
                ('name', models.CharField(choices=[('high', 'h'), ('medium', 'm'), ('low', 'l'), ('default', 'd')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField()),
                ('completed_date', models.DateTimeField(blank=True, null=True)),
                ('priority', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='todo_app.priority')),
            ],
        ),
    ]
