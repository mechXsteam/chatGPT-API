# Generated by Django 4.2.5 on 2023-09-20 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='sender',
        ),
    ]
