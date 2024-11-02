from django.shortcuts import render
from . import serializers
from rest_framework import permissions
from rest_framework import generics
from . import models
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class ProductView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.ProductSerializer

    def get(self, request):
        output = [{
            "name": output.name, 
            "description":output.description, 
            "price": output.price,
            #"image": output.image,
            } for output in models.Products.objects.all()]
        

        return Response(output)
    
    
    """def post(self, request):

        serializer = serializer.ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)"""
    

class ProductSerializerView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.ProductSerializer
    queryset = models.Products.objects.all()


class DesignView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.DesignSerializer

    def get(self, request):
        Doutput = [{
            "product": Doutput.product,
            "user": Doutput.user,
            #"design_image": Doutput.design_image,
            "is_approved": Doutput.is_approved,
            "date_created": Doutput.date_created,
        } for Doutput in models.Design.objects.all()]

        return Response(Doutput)
    

    def post(self, request):
        serializer = serializers.DesignSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

class DesignSerializerView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.DesignSerializer
    queryset = models.Order.objects.all()

class CartSerializerView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.CartItemSerializer
    queryset = models.Cart.objects.all()

class CartItemSerializerView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.CartItemSerializer
    queryset = models.CartItem.objects.all()

class OrderSerializerView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.OrderSerializer
    queryset = models.Order.objects.all()



