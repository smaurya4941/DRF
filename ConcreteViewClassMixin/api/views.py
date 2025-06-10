from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Student
from .serializers import StudentSerializer


class StudentListView(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
# This view will return a list of all students in the database.
    

class StudentCreateview(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer



class StudentRetrieveView(RetrieveAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


class StudentListCreateView(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


class StudentRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer