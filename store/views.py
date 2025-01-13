from django.shortcuts import render, get_object_or_404
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import generics, status
from .filter import *
from rest_framework import pagination #to work with pagination
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin


# Create your views here.


class AllDesignAdminView(ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    serializer_class =  UserDesignForAdmin
    queryset = UserDesign.objects.all()
    http_method_names = ['get']

class UserDesignView(ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserDesignSer
    queryset = UserDesign.objects.all()
    http_method_names = ['post']

    
    def post(self, request):
        serializer = UserDesignSer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(serializer.data)


class UDProductionView(ModelViewSet):
    #Api view used to display orderd designs for admins
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserDesignSerializer
    queryset = UserDesign.objects.all()
    http_method_names = ['get']

    def get_queryset(self):
        
        return UserDesign.objects.filter(user=self.request.user)



class ProductView(ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', 'put']

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'description', 'catagory']
    pagination_class = pagination.PageNumberPagination #allow us to crate PageNumberPagination.

    def put(self, request):
        serializer = ProducctCustemizeSer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(serializer.data)
    

class CatagoryView(ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Catagory.objects.all()
    serializer_class = CatagorySerializer
    http_method_names = ['get']


class CartView(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


    
class CartItemView(ModelViewSet):
    http_method_names = ["get", "post", "patch", "delete"]
    
    def get_queryset(self):
        return CartItem.objects.filter(cart_id=self.kwargs["cart_pk"])
    

    def get_serializer_class(self):
        if self.request.method == "POST":
            return AddCartItemSerializer
        
        elif self.request.method == "PATCH":
            return UpdateCartItmSerializer
        
        return CartItemSerializer
    
    def get_serializer_context(self):
        return {"cart_id": self.kwargs["cart_pk"]}
    

class OrderView(ModelViewSet):
    permission_classes = [permissions.AllowAny]
    http_method_names = ["get", "patch", "post", "delete", "options", "head"]
    
    def get_permissions(self):
        if self.request.method in ["PATCH", "DELETE"]:
            return [permissions.IsAuthenticated()]
        return [permissions.IsAuthenticated()]
            
    
    
    def create(self, request, *args, **kwargs):
        serializer = CreateOrderSerializer(data=request.data, context={"user_id": self.request.user.id})
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data)
        
    
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateOrderSerializer
        elif self.request.method == 'PATCH':
            return UpdateOrderSerializer
        return OrderSerializer

    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(owner=user)
    
    # def get_serializer_context(self):
    #     return {"user_id": self.request.user.id}
    




