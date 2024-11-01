from django.conf import settings
from django.conf.urls.static import static
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
    path('classifications/', ClassificationListView.as_view(), name='classification_list'),
    path('classifications/create/', ClassificationCreateView.as_view(), name='classification_create'),
    path('classifications/<int:pk>/', ClassificationDetailView.as_view(), name='classification_detail'),
    path('classifications/update/<int:pk>/', ClassificationUpdateView.as_view(), name='classification_update'),
    path('classifications/delete/<int:pk>/', ClassificationDeleteView.as_view(), name='classification_delete'),

    # Doctor
    path('', DoctorListView.as_view(), name='doctor_list'),
    path('create/', DoctorCreateView.as_view(), name='doctor_create'),
    path('<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
    path('update/<int:pk>/', DoctorUpdateView.as_view(), name='doctor_update'),
    path('delete/<int:pk>/', DoctorDeleteView.as_view(), name='doctor_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
