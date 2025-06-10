from django.shortcuts import render
from .models import Student
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def student_api(request):
    if request.method=='GET':
        id=request.data.get('id')
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
        
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)
        

    if request.method=="POST":
        data=request.data
        serializer=StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message":"data created "})
        return Response(serializer.errors, status=400)
    
    if request.method=='PUT':
        id=request.data.get('id')
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message":"data updated "})
        return Response(serializer.errors)
    
    if request.method=='DELETE':
        id=request.data.get("id")
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({"Message":"data deleted "})


