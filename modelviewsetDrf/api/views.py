from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
#View student list


class StudentModelViewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

#FOr read only viewset(List and retrieve)
    
# class StudentModelViewset(viewsets.ReadOnlyModelViewSet):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer