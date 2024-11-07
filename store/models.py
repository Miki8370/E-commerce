from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Catagory(models.Model):
    name = models.CharField(max_length=100)

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
    category = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    
    # Fixed price for all user-designed products
    price = models.DecimalField(max_digits=10, decimal_places=2, default=29.99)  # Fixed, non-editable

    def __str__(self):
        return self.description


class UserDesign(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Size = models.ForeignKey(Size, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    #product_image = models.ImageField(upload_to='designs/')
    shipping_address = models.TextField()
    crated_at = models.DateField(auto_now_add=True)
    

    def __str__(self):
        
        return self.shipping_address



class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    user_design = models.ForeignKey(UserDesign, on_delete=models.CASCADE)

    def get_total_price(self):
        return self.quantity * self.product.price

# Cart model linked to the user
class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)

    def get_cart_total(self):
        return sum(item.get_total_price() for item in self.items.all())

# Order model
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    payment_details = models.TextField()  # Could be expanded to more detailed fields

    def get_order_total(self):
        return self.cart.get_cart_total()