from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Classification, Doctor
from .forms import ClassificationForm, DoctorForm


# CLASSIFICATION
class ClassificationListView(ListView):
    model = Classification
    template_name = 'classification_list.html'  # Укажите путь к вашему шаблону
    context_object_name = 'classifications'


class ClassificationCreateView(CreateView):
    model = Classification
    form_class = ClassificationForm
    template_name = 'classification_form.html'  # Укажите путь к вашему шаблону
    success_url = reverse_lazy('classification_list')  # Замените на имя вашего URL


class ClassificationDetailView(DetailView):
    model = Classification
    template_name = 'classification_detail.html'  # Укажите путь к вашему шаблону
    context_object_name = 'classification'


class ClassificationUpdateView(UpdateView):
    model = Classification
    form_class = ClassificationForm
    template_name = 'classification_form.html'  # Укажите путь к вашему шаблону
    success_url = reverse_lazy('classification_list')  # Замените на имя вашего URL


class ClassificationDeleteView(DeleteView):
    model = Classification
    template_name = 'classification_confirm_delete.html'  # Укажите путь к вашему шаблону
    success_url = reverse_lazy('classification_list')  # Замените на имя вашего URL


# DOCTOR
class DoctorListView(ListView):
    model = Doctor
    template_name = 'doctor_list.html'  # Укажите путь к вашему шаблону
    context_object_name = 'doctors'


class DoctorCreateView(CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctor_form.html'  # Укажите путь к вашему шаблону
    success_url = reverse_lazy('doctor_list')  # Замените на имя вашего URL


class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'doctor_detail.html'  # Укажите путь к вашему шаблону
    context_object_name = 'doctor'


class DoctorUpdateView(UpdateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctor_form.html'  # Укажите путь к вашему шаблону
    success_url = reverse_lazy('doctor_list')  # Замените на имя вашего URL


class DoctorDeleteView(DeleteView):
    model = Doctor
    template_name = 'doctor_confirm_delete.html'  # Укажите путь к вашему шаблону
    success_url = reverse_lazy('doctor_list')  # Замените на имя вашего URL
