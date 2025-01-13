from django.shortcuts import render
from . serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from . models import *
from rest_framework.viewsets import ModelViewSet
# Create your views here.


        
class DesignViewSet(ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserDesignSerializer
    http_method_names = ['post']
    