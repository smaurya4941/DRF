from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
# Model Object-single student data
def student_detail(request,pk):
    stu=Student.objects.get(id=pk)  #getting object of student with id=1
    # print(stu)
    serializer=StudentSerializer(stu)  #converted model object into python data type (Serialisation)
    # print(serializer.data)
    json_data=JSONRenderer().render(serializer.data) #converted python data into JSON format
    # print(json_data)
    return HttpResponse(json_data,content_type='application/json') #returning JSON data as response
 


# Queryset -All student data
def student_list(request):
    stu=Student.objects.all()  #getting object of all students
    serializer=StudentSerializer(stu,many=True)  #converted model object into python data type(Serialisation)
    json_data=JSONRenderer().render(serializer.data) #converted python data into JSON format
    return HttpResponse(json_data,content_type='application/json') #returning JSON data as response

    #instead of above 2 llines we can use below line
    # return JsonResponse(serializer.data,safe=False) #returning JSON data as response        