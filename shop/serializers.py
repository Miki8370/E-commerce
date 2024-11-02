from rest_framework import serializers
from . import models


class ProductSerializer(serializers.ModelSerializer):
    #created = serializers.ReadOnlyField()    
    #completed = serializers.ReadOnlyField()
    class Meta:
        fields = [
    
        'name',
        'description',
        'price',
        'image',
        'available_sizes',
        'available_colors',
        'is_customizable',
        'created_by',
        'date_added',
        ]
        model = models.Products


class DesignSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'product',
            'user',
            'design_image',
            'is_approved',
            'date_created',

        ]

        model = models.Design

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'user',
            'items',
            'total_price',
        ]

        model = models.Cart

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'product',
            'quantity',
            'design',
        ]

        model = models.CartItem
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'user',
            'cart',
            'shipping_address',
            'status',
            'date_ordered',
        ]

        model = models.Order


