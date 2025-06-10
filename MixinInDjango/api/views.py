from .models import Student
from .serializers import StudentSerializer
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import GenericAPIView

#View student list
class StudentList(GenericAPIView,ListModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)


#For POST
class StudentCreate(GenericAPIView,CreateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


#to retrieve single data(GET) 
class StudentRetrieve(GenericAPIView,RetrieveModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

#to update  data(PUT PATCH) 
class StudentPUT(GenericAPIView,UpdateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)


#To delete data(DELETE)
class StudentDelete(GenericAPIView,DestroyModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)


#######################################################################################
#All the above functionality in two class
    

#CLass 1:::LISt + CReate ===>Pk not required
class StudentListandCreate(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
#Class 2:::Retrieve + Update + Delete ===>Pk required

class StudentRetrieveDestroyUpdate(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
