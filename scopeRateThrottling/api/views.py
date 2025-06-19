from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework.throttling import ScopedRateThrottle

class StudentListView(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='viewStuThrottle'
# This view will return a list of all students in the database.
    

class StudentCreateview(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    # throttle_scope='viewStuThrottle'



class StudentRetrieveView(RetrieveAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='viewStuThrottle'


class StudentListCreateView(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    


class StudentRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='modifyApi'

class StudentRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='modifyApi'