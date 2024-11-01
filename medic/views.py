from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from doctors.models import Doctor
from .models import Diagnostic, Record, Result
from .forms import DiagnosticForm, RecordForm, ResultForm


# Main
def main_view(request):
    doctors = Doctor.objects.all()[:3]
    diagnostics = Diagnostic.objects.filter(id__in=[4, 5, 6])
    context = {
        'doctors': doctors,
        'diagnostics': diagnostics,
    }
    return render(request, 'medic/main.html', context)


# DIAGNOSTIC
class DiagnosticListView(ListView):
    model = Diagnostic
    template_name = 'medic/diagnostic_list.html'
    context_object_name = 'diagnostics'


class DiagnosticCreateView(CreateView):
    model = Diagnostic
    form_class = DiagnosticForm
    template_name = 'medic/diagnostic_form.html'
    success_url = reverse_lazy('medic:diagnostic_list')


class DiagnosticDetailView(DetailView):
    model = Diagnostic
    template_name = 'medic/diagnostic_detail.html'
    context_object_name = 'diagnostic'


class DiagnosticUpdateView(UpdateView):
    model = Diagnostic
    form_class = DiagnosticForm
    template_name = 'medic/diagnostic_form.html'
    success_url = reverse_lazy('medic:diagnostic_list')


class DiagnosticDeleteView(DeleteView):
    model = Diagnostic
    template_name = 'medic/diagnostic_confirm_delete.html'
    success_url = reverse_lazy('diagnostic_list')


# RECORD
class RecordListView(ListView):
    model = Record
    template_name = 'medic/record_list.html'
    context_object_name = 'records'


class RecordCreateView(CreateView):
    model = Record
    form_class = RecordForm
    template_name = 'medic/record_form.html'
    success_url = reverse_lazy('medic:record_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем врачей и диагностику в контекст
        context['doctors'] = Doctor.objects.all()
        context['diagnostics'] = Diagnostic.objects.all()
        return context

    def form_valid(self, form):
        # Устанавливаем текущего пользователя как пациента
        form.instance.patient = self.request.user
        return super().form_valid(form)


class RecordDetailView(DetailView):
    model = Record
    template_name = 'medic/record_detail.html'
    context_object_name = 'record'


class RecordUpdateView(UpdateView):
    model = Record
    form_class = RecordForm
    template_name = 'medic/record_form.html'
    success_url = reverse_lazy('record_list')


class RecordDeleteView(DeleteView):
    model = Record
    template_name = 'record_confirm_delete.html'
    success_url = reverse_lazy('record_list')


# RESULT
class ResultListView(ListView):
    model = Result
    template_name = 'medic/result_list.html'
    context_object_name = 'results'


class ResultCreateView(CreateView):
    model = Result
    form_class = ResultForm
    template_name = 'medic/result_form.html'
    success_url = reverse_lazy('result_list')


class ResultDetailView(DetailView):
    model = Result
    template_name = 'medic/result_detail.html'
    context_object_name = 'result'


class ResultUpdateView(UpdateView):
    model = Result
    form_class = ResultForm
    template_name = 'medic/result_form.html'
    success_url = reverse_lazy('result_list')


class ResultDeleteView(DeleteView):
    model = Result
    template_name = 'result_confirm_delete.html'
    success_url = reverse_lazy('result_list')
