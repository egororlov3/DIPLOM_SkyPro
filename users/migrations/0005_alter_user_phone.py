# Generated by Django 5.1.2 on 2024-10-31 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(default='unknown', max_length=35, verbose_name='телефон'),
        ),
    ]