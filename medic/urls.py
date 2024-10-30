from django.urls import path
from .views import (
    DiagnosticListView, DiagnosticCreateView, DiagnosticDetailView, DiagnosticUpdateView, DiagnosticDeleteView,
    RecordListView, RecordCreateView, RecordDetailView, RecordUpdateView, RecordDeleteView,
    ResultListView, ResultCreateView, ResultDetailView, ResultUpdateView, ResultDeleteView
)

app_name = 'medic'

urlpatterns = [
    # Diagnostic
    path('diagnostics/', DiagnosticListView.as_view(), name='diagnostic-list'),
    path('diagnostics/create/', DiagnosticCreateView.as_view(), name='diagnostic-create'),
    path('diagnostics/<int:pk>/', DiagnosticDetailView.as_view(), name='diagnostic-detail'),
    path('diagnostics/update/<int:pk>/', DiagnosticUpdateView.as_view(), name='diagnostic-update'),
    path('diagnostics/delete/<int:pk>/', DiagnosticDeleteView.as_view(), name='diagnostic-delete'),

    # Record
    path('records/', RecordListView.as_view(), name='record-list'),
    path('records/create/', RecordCreateView.as_view(), name='record-create'),
    path('records/<int:pk>/', RecordDetailView.as_view(), name='record-detail'),
    path('records/update/<int:pk>/', RecordUpdateView.as_view(), name='record-update'),
    path('records/delete/<int:pk>/', RecordDeleteView.as_view(), name='record-delete'),

    # Result
    path('results/', ResultListView.as_view(), name='result-list'),
    path('results/create/', ResultCreateView.as_view(), name='result-create'),
    path('results/<int:pk>/', ResultDetailView.as_view(), name='result-detail'),
    path('results/update/<int:pk>/', ResultUpdateView.as_view(), name='result-update'),
    path('results/delete/<int:pk>/', ResultDeleteView.as_view(), name='result-delete'),
]
