# Generated by Django 3.1 on 2020-09-30 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mess', '0002_auto_20200930_1935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cancel_model',
            name='enddate',
        ),
        migrations.RemoveField(
            model_name='cancel_model',
            name='startdate',
        ),
    ]