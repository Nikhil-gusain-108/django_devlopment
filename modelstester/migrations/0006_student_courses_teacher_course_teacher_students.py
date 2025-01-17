# Generated by Django 5.0.6 on 2024-06-24 05:50

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelstester', '0005_remove_student_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(related_name='students', to='modelstester.courses'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='course',
            field=models.OneToOneField(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='modelstester.courses'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='students',
            field=models.ManyToManyField(to='modelstester.student'),
        ),
    ]
