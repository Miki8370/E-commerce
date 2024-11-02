from django.shortcuts import render
from . serializers import *
from . models import *
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.contrib.auth.models import User

# Create your views here.


class CustomProductView(APIView):
    permission_classes = [permissions.AllowAny]


    def get(self, request):
        product = CustomMadeProducts.objects.all()
        serializer = CustomProductSerializer(product, many=True)
        return Response(serializer.data)
    
