from django.urls import path
from .views import (
    ClassificationListView,
    ClassificationCreateView,
    ClassificationDetailView,
    ClassificationUpdateView,
    ClassificationDeleteView,
    DoctorListView,
    DoctorCreateView,
    DoctorDetailView,
    DoctorUpdateView,
    DoctorDeleteView,
)

app_name = 'doctors'


urlpatterns = [
    # Classification
    path('classifications/', ClassificationListView.as_view(), name='classification-list'),
    path('classifications/create/', ClassificationCreateView.as_view(), name='classification-create'),
    path('classifications/<int:pk>/', ClassificationDetailView.as_view(), name='classification-detail'),
    path('classifications/update/<int:pk>/', ClassificationUpdateView.as_view(), name='classification-update'),
    path('classifications/delete/<int:pk>/', ClassificationDeleteView.as_view(), name='classification-delete'),

    # Doctor
    path('doctors/', DoctorListView.as_view(), name='doctor-list'),
    path('doctors/create/', DoctorCreateView.as_view(), name='doctor-create'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),
    path('doctors/update/<int:pk>/', DoctorUpdateView.as_view(), name='doctor-update'),
    path('doctors/delete/<int:pk>/', DoctorDeleteView.as_view(), name='doctor-delete'),
]
