# Generated by Django 5.0.6 on 2024-07-03 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_details',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user_details',
            name='last_name',
        ),
    ]
