from django.shortcuts import render
from . import serializers
from rest_framework import permissions
from rest_framework import generics
from . import models

# Create your views here.

class ProductSerializerView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.ProductSerializer
    queryset = models.Products.objects.all()
