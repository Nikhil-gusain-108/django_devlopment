# Generated by Django 5.0.6 on 2024-06-22 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='card_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=10)),
                ('discription', models.CharField(max_length=100)),
            ],
        ),
    ]