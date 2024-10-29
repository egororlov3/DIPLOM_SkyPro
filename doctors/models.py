from django.db import models
from users.models import NULLABLE


class Classification(models.Model):
    title = models.CharField(max_length=250, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f"{self.title}: {self.description}"

    class Meta:
        verbose_name = 'классификиция'
        verbose_name_plural = 'классификиции'


class Doctor(models.Model):
    full_name = models.CharField(max_length=250, verbose_name='ФИО')
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE, verbose_name='классификация')
    years = models.IntegerField(verbose_name='лет опыта')
    months = models.IntegerField(verbose_name='месяцев опыта')
    image = models.ImageField(upload_to='#', **NULLABLE, verbose_name='аватар')

    def __str__(self):
        return f"{self.full_name} ({self.classification}), работает {self.years} лет и {self.months} месяцев"

    class Meta:
        verbose_name = 'врач'
        verbose_name_plural = 'врачи'
