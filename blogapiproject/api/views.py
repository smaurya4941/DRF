from django.shortcuts import render

# Create your views here.
from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets

#authentication and permissions
from rest_framework.authentication import SessionAuthentication
# from rest_framework.permissions import IsAuthenticatedOrReadOnly

#custom permission
from rest_framework.permissions import BasePermission ,SAFE_METHODS

class CustomPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        #if Safe method then allow
        if request.method in SAFE_METHODS:
            return True
        if request.user==obj.author:
            return True




class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[CustomPermission]