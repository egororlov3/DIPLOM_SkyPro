# Generated by Django 5.1.2 on 2024-10-29 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
