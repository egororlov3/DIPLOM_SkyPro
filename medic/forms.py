from django import forms
from .models import Diagnostic, Record, Result


class DiagnosticForm(forms.ModelForm):
    class Meta:
        model = Diagnostic
        fields = ['title', 'description', 'price', 'image']
        labels = {
            'title': 'Название диагностики',
            'description': 'Описание',
            'price': 'Цена',
            'image': 'Фото',
        }


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['patient', 'diagnostic', 'date', 'doctors', 'wishes']
        labels = {
            'patient': 'Пациент',
            'diagnostic': 'Диагностика',
            'date': 'Дата записи',
            'doctors': 'Врач',
            'wishes': 'Пожелания',
        }


class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['title', 'patient', 'result', 'description', 'medication']
        labels = {
            'title': 'Название результатов',
            'patient': 'Пациент',
            'result': 'Результат',
            'description': 'Описание',
            'medication': 'Лечение',
        }
