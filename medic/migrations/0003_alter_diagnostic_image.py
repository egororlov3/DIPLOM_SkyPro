# Generated by Django 5.1.2 on 2024-10-30 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medic', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnostic',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='фото'),
        ),
    ]
