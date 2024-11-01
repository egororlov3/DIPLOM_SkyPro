# Generated by Django 5.1.2 on 2024-10-31 14:30

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medic', '0005_record_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='дата результатов'),
        ),
    ]