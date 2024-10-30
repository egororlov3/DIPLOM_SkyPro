from django import forms
from .models import Classification, Doctor

class ClassificationForm(forms.ModelForm):
    class Meta:
        model = Classification
        fields = ['title', 'description']
        labels = {
            'title': 'Название классификации',
            'description': 'Описание классификации',
        }

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['full_name', 'classification', 'years', 'months', 'image']
        labels = {
            'full_name': 'ФИО',
            'classification': 'Классификация',
            'years': 'Лет опыта',
            'months': 'Месяцев опыта',
            'image': 'Аватар',
        }
        widgets = {
            'years': forms.NumberInput(attrs={'min': 0}),
            'months': forms.NumberInput(attrs={'min': 0, 'max': 11}),
        }
