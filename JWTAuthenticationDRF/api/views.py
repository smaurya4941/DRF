from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

#Note:to apply basic authentication in all classes then we define it globally in settings.py file
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    
  

#eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ5NjQzNzU0LCJpYXQiOjE3NDk2NDIxOTUsImp0aSI6IjdhODdmNjIzODZjYzQ0OTU5ODc1MGE0OTk2MDE4Nzc2IiwidXNlcl9pZCI6MX0.CwZh5rc_15uT8I7ns-3WoD6Kp0Mj_23_FNGtstJtGDk
    
    # eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ5NjQ0MDk0LCJpYXQiOjE3NDk2NDIxOTUsImp0aSI6IjU3M2ZjNzE0ZGJmMjQ1YmM5NzViYjQxOTMwMGNjMzdjIiwidXNlcl9pZCI6MX0.qlP__N_KsIxr1rmo1SRD2c6T45lnjpWl1SwjgFZPkPA