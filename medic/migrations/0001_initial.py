# Generated by Django 5.1.2 on 2024-10-29 19:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnostic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название')),
                ('description', models.TextField(verbose_name='описание')),
                ('price', models.IntegerField(verbose_name='цена')),
                ('image', models.ImageField(blank=True, null=True, upload_to='#', verbose_name='фото')),
            ],
            options={
                'verbose_name': 'диагностика',
                'verbose_name_plural': 'диагностики',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='название результатов')),
                ('result', models.TextField(verbose_name='результат')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('medication', models.TextField(verbose_name='лечение')),
            ],
            options={
                'verbose_name': 'результат',
                'verbose_name_plural': 'результаты',
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='дата записи')),
                ('wishes', models.TextField(blank=True, null=True, verbose_name='пожелания')),
                ('diagnostic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medic.diagnostic', verbose_name='диагностика')),
                ('doctors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.doctor', verbose_name='врачи')),
            ],
            options={
                'verbose_name': 'запись на диагонстику',
                'verbose_name_plural': 'записи на диагонстику',
            },
        ),
    ]
