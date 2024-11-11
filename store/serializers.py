from rest_framework import serializers
from . models import *


class UserDesignSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = UserDesign


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Product
        extra_kwargs = {
            'name': {'read_only': True},
            'description': {'read_only': True},
            'price': {'read_only': True},
            'image': {'read_only': True},
            #'is_customizable': {'read_only': False},
            'created_by': {'read_only': True},
            'date_added': {'read_only': True},
            #'available_sizes': {'read_only': False},
            #'available_colors': {'read_only': False},
            'category': {'read_only': True},


        }
        

    category = serializers.StringRelatedField() #changes the relationship from id to the name
    #available_sizes = serializers.StringRelatedField()
    #available_colors = serializers.StringRelatedField()
    created_by = serializers.StringRelatedField()
    



class CartProductListSerializer(serializers.ModelSerializer):#created to only small data for my cart api
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']



class CatagorySerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = '__all__'
        model = Catagory



class CartItemSerializer(serializers.ModelSerializer):
    product = CartProductListSerializer(many=False) #allows to list all product instance in the cart api 
    sub_total = serializers.SerializerMethodField( method_name="total")
    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product', 'quantity', 'sub_total']

    def total(self, cartitem:CartItem):
        return cartitem.quantity * cartitem.product.price

class AddCartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()
    def validate_product_id(self, value):
        if not Product.objects.filter(pk=value).exists():
            raise serializers.ValidationError("There is no product associated with the given ID")
        
        return value

    def save(self, **kwargs):
        cart_id = self.context["cart_id"]
        product_id = self.validated_data["product_id"] 
        quantity = self.validated_data["quantity"] 
        
        try:
            cartitem = CartItem.objects.get(product_id=product_id, cart_id=cart_id)
            cartitem.quantity += quantity
            cartitem.save()
            
            self.instance = cartitem
            
        
        except:
            
            self.instance = CartItem.objects.create(cart_id=cart_id, **self.validated_data)
            
        return self.instance
    class Meta:
        model = CartItem
        fields = ['id', 'product_id', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only = True)
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField(method_name='main_total')

    class Meta:
        model = Cart
        fields = ['id', 'items', 'total_price']

    def main_total(self, cart: Cart):
        items = cart.items.all()
        total = sum([item.quantity * item.product.price for item in items])
        return total

        

