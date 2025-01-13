from django.shortcuts import render
from . serializers import *
from . models import *
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet


# Create your views here.


    

class CustomProductsView(ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomProductSerializer
    queryset = CustomMadeProducts.objects.all()
    http_method_names = ['get']
