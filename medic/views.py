from rest_framework import generics
from .models import Diagnostic, Record, Result
from .serializers import DiagnosticSerializer, RecordSerializer, ResultSerializer


# Diagnostic
class DiagnosticListView(generics.ListAPIView):
    queryset = Diagnostic.objects.all()
    serializer_class = DiagnosticSerializer


class DiagnosticCreateView(generics.CreateAPIView):
    queryset = Diagnostic.objects.all()
    serializer_class = DiagnosticSerializer


class DiagnosticDetailView(generics.RetrieveAPIView):
    queryset = Diagnostic.objects.all()
    serializer_class = DiagnosticSerializer


class DiagnosticUpdateView(generics.UpdateAPIView):
    queryset = Diagnostic.objects.all()
    serializer_class = DiagnosticSerializer


class DiagnosticDeleteView(generics.DestroyAPIView):
    queryset = Diagnostic.objects.all()
    serializer_class = DiagnosticSerializer


# Record
class RecordListView(generics.ListAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class RecordCreateView(generics.CreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class RecordDetailView(generics.RetrieveAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class RecordUpdateView(generics.UpdateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class RecordDeleteView(generics.DestroyAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


# Result
class ResultListView(generics.ListAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


class ResultCreateView(generics.CreateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


class ResultDetailView(generics.RetrieveAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


class ResultUpdateView(generics.UpdateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


class ResultDeleteView(generics.DestroyAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
