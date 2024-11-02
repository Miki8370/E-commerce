from django.db import models
from django.contrib.auth.models import User
# Create your models here.

"""
class Product(models.Model):
    name = models.CharField(max_length=100)

class Catagory(models.Model):
    catagory_name = models.CharField(max_length=100)

    def __str__(self):
        return self.catagory_name

"""

class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    available_sizes = models.CharField(max_length=100)  # "S, M, L, XL"
    available_colors = models.CharField(max_length=100)  # "Red, Blue, Black"
    is_customizable = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    #catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    

class Design(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Designer/owner
    design_image = models.ImageField(upload_to='designs/')
    is_approved = models.BooleanField(default=False)  # For admin to approve if needed
    date_created = models.DateTimeField(auto_now_add=True)



class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='shop_orders')
    items = models.ManyToManyField('CartItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class CartItem(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    design = models.ForeignKey(Design, on_delete=models.SET_NULL, null=True, blank=True)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    shipping_address = models.TextField()
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('shipped', 'Shipped'), ('delivered', 'Delivered')])
    date_ordered = models.DateTimeField(auto_now_add=True)
