# Generated by Django 5.0.6 on 2024-06-24 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelstester', '0003_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='courses',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='students',
        ),
    ]
