# Generated by Django 5.1.1 on 2024-09-14 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermaster',
            name='username',
        ),
    ]
