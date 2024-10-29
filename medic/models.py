from django.db import models
from django.conf import settings
from doctors.models import Doctor
from users.models import NULLABLE


# Диагностики
class Diagnostic(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    price = models.IntegerField(verbose_name='цена')
    image = models.ImageField(upload_to='#', **NULLABLE, verbose_name='фото')

    def __str__(self):
        return f"{self.title} {self.description} {self.price}"

    class Meta:
        verbose_name = 'диагностика'
        verbose_name_plural = 'диагностики'


# Запись на диагонстику
class Record(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пациент')
    diagnostic = models.ForeignKey(Diagnostic, on_delete=models.CASCADE, verbose_name='диагностика')
    date = models.DateField(verbose_name='дата записи')
    doctors = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='врачи')
    wishes = models.TextField(**NULLABLE, verbose_name='пожелания')

    def __str__(self):
        return f"{self.patient} записался/записалась на {self.diagnostic} к врачу {self.doctors}, дата: {self.date}"

    class Meta:
        verbose_name = 'запись на диагонстику'
        verbose_name_plural = 'записи на диагонстику'


# Результаты
class Result(models.Model):
    title = models.CharField(max_length=200, verbose_name='название результатов')
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пациент')
    result = models.TextField(verbose_name='результат')
    description = models.TextField(**NULLABLE, verbose_name='описание')
    medication = models.TextField(verbose_name='лечение')

    def __str__(self):
        return f"{self.title} {self.result} {self.medication}, пациенту: {self.patient}"

    class Meta:
        verbose_name = 'результат'
        verbose_name_plural = 'результаты'
