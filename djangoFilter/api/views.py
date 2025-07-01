from django.shortcuts import render

# Create your views here.
from .models import Student
from .serializers import StudentSerializers
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.generics import ListAPIView
class StudentListView(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    filterset_fields=['city']


#For per view filtering
class StudentListView(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['city']
