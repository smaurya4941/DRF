from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly


#Note:to apply basic authentication in all classes then we define it globally in settings.py file
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    #BAasic authentication and permission for class
    authentication_classes=[BasicAuthentication]
    # permission_classes=[IsAuthenticated] #for login user only
    # permission_classes=[AllowAny] #`for all user`
    # permission_classes=[IsAdminUser] #for isStaff true user only
    permission_classes=[IsAuthenticatedOrReadOnly]


# class StudentModelViewSet2(viewsets.ModelViewSet):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
#     #BAasic authentication and permission can be over write global permission and authentication
#     authentication_classes=[BasicAuthentication]
#     permission_classes=[AllowAny]