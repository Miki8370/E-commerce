"""
from django.db import models
from django.contrib.auth.models import User

class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Custom-made product price
    image = models.ImageField(upload_to='products/')
    available_sizes = models.ManyToManyField(Size, blank=True)
    available_colors = models.ManyToManyField(Color, blank=True)
    is_customizable = models.BooleanField(default=False)  # Only for products that can be customized
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Design(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Designer/owner
    design_image = models.ImageField(upload_to='designs/')
    is_approved = models.BooleanField(default=False)  # Admin approval for user designs
    date_created = models.DateTimeField(auto_now_add=True)
    
    # Fixed price for all user-designed products
    price = models.DecimalField(max_digits=10, decimal_places=2, default=29.99)  # Fixed, non-editable

    def __str__(self):
        return f"{self.user.username}'s design on {self.product.name}"




class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='shop_orders')
    items = models.ManyToManyField('CartItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    design = models.ForeignKey(Design, on_delete=models.SET_NULL, null=True, blank=True)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    shipping_address = models.TextField()
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('shipped', 'Shipped'), ('delivered', 'Delivered')])
    date_ordered = models.DateTimeField(auto_now_add=True)

"""