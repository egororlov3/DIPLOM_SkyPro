from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Classification, Doctor
from .forms import ClassificationForm, DoctorForm


# CLASSIFICATION
class ClassificationListView(ListView):
    model = Classification
    template_name = 'doctors/classification_list.html'
    context_object_name = 'classifications'


class ClassificationCreateView(CreateView):
    model = Classification
    form_class = ClassificationForm
    template_name = 'doctors/classification_form.html'
    success_url = reverse_lazy('classification_list')


class ClassificationDetailView(DetailView):
    model = Classification
    template_name = 'doctors/classification_detail.html'
    context_object_name = 'classification'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        classification = self.get_object()
        context['doctors'] = Doctor.objects.filter(classification=classification)
        return context


class ClassificationUpdateView(UpdateView):
    model = Classification
    form_class = ClassificationForm
    template_name = 'doctors/classification_form.html'
    success_url = reverse_lazy('classification_list')


class ClassificationDeleteView(DeleteView):
    model = Classification
    template_name = 'doctors/classification_confirm_delete.html'
    success_url = reverse_lazy('classification_list')


# DOCTOR
class DoctorListView(ListView):
    model = Doctor
    template_name = 'doctors/doctor_list.html'
    context_object_name = 'doctors'

    def get_queryset(self):
        queryset = super().get_queryset()
        classification_filter = self.request.GET.get('classification')

        if classification_filter:
            queryset = queryset.filter(classification__title=classification_filter)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Получаем список классификаций
        context['classifications'] = Doctor.objects.values_list('classification__title', flat=True).distinct()
        context['selected_classification'] = self.request.GET.get('classification')
        return context


class DoctorCreateView(CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctors/doctor_form.html'
    success_url = reverse_lazy('doctor_list')


class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'doctors/doctor_detail.html'
    context_object_name = 'doctor'


class DoctorUpdateView(UpdateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctors/doctor_form.html'
    success_url = reverse_lazy('doctor_list')


class DoctorDeleteView(DeleteView):
    model = Doctor
    template_name = 'doctors/doctor_confirm_delete.html'
    success_url = reverse_lazy('doctor_list')
