from django.shortcuts import render

# Create your views here.
from .models import Student
from .serializers import StudentSerializers

from rest_framework.generics import ListAPIView

# class StudentListView(ListAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializers


# class StudentListView(ListAPIView):
#     queryset=Student.objects.filter(passby='user2')
#     serializer_class=StudentSerializers



class StudentListView(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers

    def get_queryset(self):    #filter only those student # who are passed by the current logged in user/teacher user
        user=self.request.user
        return Student.objects.filter(passby=user)