from rest_framework import generics
from .models import Classification, Doctor
from .serializers import ClassificationSerializer, DoctorSerializer


# Classification
class ClassificationListView(generics.ListAPIView):
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer


class ClassificationCreateView(generics.CreateAPIView):
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer


class ClassificationDetailView(generics.RetrieveAPIView):
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer


class ClassificationUpdateView(generics.UpdateAPIView):
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer


class ClassificationDeleteView(generics.DestroyAPIView):
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer


# Doctor
class DoctorListView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorCreateView(generics.CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorDetailView(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorUpdateView(generics.UpdateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorDeleteView(generics.DestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
