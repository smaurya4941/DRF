from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


#GEt method # @api_view(['GET'])
# @api_view()
# def hello(request):
#     return Response({"message": "Hello, World!"})


# @api_view(['GET'])
# def hello(request):
#     return Response({"message": "Hello, World!"})


#POSt method
@api_view(['GET','POST'])
def hello(request):
    if request.method=='GET':
        print("GET request received")
        return Response({"message": "Get Method called !"})
    if request.method=='POST':
        data=request.data
        print("Received Data:", data)
        return Response({"message": "POST Method is called","data":data})
