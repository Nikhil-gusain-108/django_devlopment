# Generated by Django 5.0.6 on 2024-06-24 05:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelstester', '0006_student_courses_teacher_course_teacher_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='course',
            field=models.OneToOneField(default='no name', on_delete=django.db.models.deletion.CASCADE, to='modelstester.courses'),
        ),
    ]