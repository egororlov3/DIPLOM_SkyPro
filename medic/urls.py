from django.urls import path
from .views import (
    main_view,
    DiagnosticListView, DiagnosticCreateView, DiagnosticDetailView,
    DiagnosticUpdateView, DiagnosticDeleteView,
    RecordListView, RecordCreateView, RecordDetailView,
    RecordUpdateView, RecordDeleteView,
    ResultListView, ResultCreateView, ResultDetailView,
    ResultUpdateView, ResultDeleteView,
)

app_name = 'medic'

urlpatterns = [
    # Main view
    path('', main_view, name='main'),

    # Diagnostic URLs
    path('diagnostics/', DiagnosticListView.as_view(), name='diagnostic_list'),
    path('diagnostics/create/', DiagnosticCreateView.as_view(), name='diagnostic_create'),
    path('diagnostics/<int:pk>/', DiagnosticDetailView.as_view(), name='diagnostic_detail'),
    path('diagnostics/<int:pk>/update/', DiagnosticUpdateView.as_view(), name='diagnostic_update'),
    path('diagnostics/<int:pk>/delete/', DiagnosticDeleteView.as_view(), name='diagnostic_delete'),

    # Record URLs
    path('records/', RecordListView.as_view(), name='record_list'),
    path('records/create/', RecordCreateView.as_view(), name='record_create'),
    path('records/<int:pk>/', RecordDetailView.as_view(), name='record_detail'),
    path('records/<int:pk>/update/', RecordUpdateView.as_view(), name='record_update'),
    path('records/<int:pk>/delete/', RecordDeleteView.as_view(), name='record_delete'),

    # Result URLs
    path('results/', ResultListView.as_view(), name='result_list'),
    path('results/create/', ResultCreateView.as_view(), name='result_create'),
    path('results/<int:pk>/', ResultDetailView.as_view(), name='result_detail'),
    path('results/<int:pk>/update/', ResultUpdateView.as_view(), name='result_update'),
    path('results/<int:pk>/delete/', ResultDeleteView.as_view(), name='result_delete'),
]
