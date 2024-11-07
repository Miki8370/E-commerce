from django.shortcuts import render, get_object_or_404
from . serializers import *
from . models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import generics
from . filter import *

# Create your views here.

class UserDesignView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserDesignSerializer

    
    def post(self, request):
        serializer = UserDesignSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(serializer.data)


class UDProductionView(APIView):
    #Api view used to display orderd designs for admins
    permission_classes = [permissions.AllowAny]
    serializer_class = UserDesignSerializer


    def get(self, request):
        product = UserDesign.objects.all()
        serializer = UserDesignSerializer(product, many=True)
        return Response(serializer.data)


class UDProductDeatailView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk):
        product = get_object_or_404(UserDesign, id=pk)
        serializer = UserDesignSerializer(product)

        return Response(serializer.data)

    

class ProductView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'description']
    

"""
def get(self, request):
        
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
"""
    
    

class ProductDetailView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk):
        #product = Product.objects.get(id=pk)
        product = get_object_or_404(Product, id=pk) #get_object_or_404 is used to show proper error massage
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    
class CatagoryView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        catagory = Catagory.objects.all()
        serializer = CatagorySerializer(catagory, many=True)
        return Response(serializer.data)


class CatgoryDetailView(APIView):
    permission_classes = [permissions.AllowAny]


    def get(self, request, pk):
        catagory = get_object_or_404(Catagory, id=pk)
        serializer = CatagorySerializer(catagory)
        return Response(serializer.data)
    
