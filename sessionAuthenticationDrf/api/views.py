from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly 


#Note:to apply basic authentication in all classes then we define it globally in settings.py file
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    #Session Authentication
    authentication_classes=[SessionAuthentication]
    # permission_classes=[IsAuthenticated]
    # permission_classes=[IsAuthenticatedOrReadOnly]
    # permission_classes=[DjangoModelPermissions] #works at model level 
    permission_classes=[DjangoModelPermissionsOrAnonReadOnly] #works at model level 
