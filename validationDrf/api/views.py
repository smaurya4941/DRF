from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def student_api(request):
    if request.method=='GET':  #read
        id = request.GET.get('id', None)
        if id is not None:
            # Get a specific student
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
    
    #post method
    if request.method == 'POST':
        try:
            stream = io.BytesIO(request.body)
            python_data = JSONParser().parse(stream)
        except Exception as e:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        serializer = StudentSerializer(data=python_data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg': 'Data Created'}, status=201)
        else:
            print("Serializer Errors:", serializer.errors)  # Print the issue
            return JsonResponse(serializer.errors, status=400)
        
    #update method
    if request.method=='PUT':
        try:
            stream = io.BytesIO(request.body)
            python_data = JSONParser().parse(stream)
            id=python_data.get('id')
            stu=Student.objects.get(id=id)
        except Exception as e:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        serializer = StudentSerializer(instance=stu,data=python_data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg': 'Data Updated'}, status=201)
        else:
            print("Serializer Errors:", serializer.errors)  # Print the issue
            return JsonResponse(serializer.errors, status=400)
        
    #delete method
    if request.method=='DELETE':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        return JsonResponse({'msg':'Data Deleted'},status=204)
        
