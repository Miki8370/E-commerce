from django.shortcuts import render, get_object_or_404
from . serializers import *
from . models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import generics, status
from . filter import *
from rest_framework import pagination #to work with pagination
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin


# Create your views here.

class UserDesignView(ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserDesignSerializer

    
    def post(self, request):
        serializer = UserDesignSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(serializer.data)


class UDProductionView(ModelViewSet):
    #Api view used to display orderd designs for admins
    permission_classes = [permissions.AllowAny]
    serializer_class = UserDesignSerializer


    def get(self, request):
        product = UserDesign.objects.all()
        serializer = UserDesignSerializer(product, many=True)
        return Response(serializer.data)

"""
class UDProductDeatailView(ModelViewSet):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk):
        product = get_object_or_404(UserDesign, id=pk)
        serializer = UserDesignSerializer(product)

        return Response(serializer.data)
"""




class ProductView(ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', 'patch']

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'description']
    pagination_class = pagination.PageNumberPagination #allow us to crate PageNumberPagination.
    

"""
def get(self, request):
        
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)



class ProductDetailView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk):
        #product = Product.objects.get(id=pk)
        product = get_object_or_404(Product, id=pk) #get_object_or_404 is used to show proper error massage
        serializer = ProductSerializer(product)
        return Response(serializer.data)
"""
    
    


    
    
class CatagoryView(ModelViewSet):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        catagory = Catagory.objects.all()
        serializer = CatagorySerializer(catagory, many=True)
        return Response(serializer.data)


"""
class CatgoryDetailView(APIView):
    permission_classes = [permissions.AllowAny]


    def get(self, request, pk):
        catagory = get_object_or_404(Catagory, id=pk)
        serializer = CatagorySerializer(catagory)
        return Response(serializer.data)
"""



class CartView(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

"""
class CartDetailView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk):
        cart = get_object_or_404(Cart, id=pk)
        serializers = CartSerializer(cart)
        return Response(serializers.data)
"""

    
class CartItemView(ModelViewSet):
    
    def get_queryset(self):
        return CartItem.objects.filter(cart_id=self.kwargs["cart_pk"])
    

    def get_serializer_class(self):
        if self.request.method == "POST":
            return AddCartItemSerializer
        
        return CartItemSerializer
    
    def get_serializer_context(self):
        return {"cart_id": self.kwargs["cart_pk"]}