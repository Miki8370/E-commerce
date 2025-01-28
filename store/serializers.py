from rest_framework import serializers
from . models import *
from django.db import transaction
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class UserDesignSer(serializers.ModelSerializer):
    class Meta:
        model = UserDesign
        fields = '__all__'
        #read_only_fields = ['user']

    def validate(self, attrs):
        attrs['user'] = self.context['request'].user
        return attrs #This function returns the user that sent the request

class UserDesignSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        fields = ['Size', 'color','shipping_address', 'user']
        model = UserDesign
        
class UserDesignForAdmin(serializers.ModelSerializer):
    class Meta:
        model = UserDesign
        fields = "__all__"


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
    

class ProducctCustemizeSer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['available_sizes', 'available_colors']



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

class UpdateCartItmSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['quantity']
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


class OrderItemSerializer(serializers.ModelSerializer):
    product = CartProductListSerializer()
    class Meta:
        model = OrderItem 
        fields = ["id", "product", "quantity"]
        


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order 
        fields = ['id', "placed_at", "pending_status", "owner", "items"]


class CreateOrderSerializer(serializers.Serializer): 
    cart_id = serializers.UUIDField()
    
    
    
    def validate_cart_id(self, cart_id):
        if not Cart.objects.filter(pk=cart_id).exists():
            raise serializers.ValidationError("This cart_id is invalid")
        
        elif not CartItem.objects.filter(cart_id=cart_id).exists():
            raise serializers.ValidationError("Sorry your cart is empty")
        
        return cart_id
    
    
    
    def save(self, **kwargs):
        with transaction.atomic():
            cart_id = self.validated_data["cart_id"]
            user_id = self.context["user_id"]
            order = Order.objects.create(owner_id = user_id)
            cartitems = CartItem.objects.filter(cart_id=cart_id)
            orderitems = [
                OrderItem(order=order, 
                    product=item.product, 
                    quantity=item.quantity
                    )
            for item in cartitems
            ]
            OrderItem.objects.bulk_create(orderitems)
            # Cart.objects.filter(id=cart_id).delete()
            return order


class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order 
        fields = ["pending_status"]