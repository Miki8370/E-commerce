from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
import uuid

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
    available_sizes = models.ForeignKey(Size, on_delete=models.CASCADE, null=True, blank=True, default=1)
    available_colors = models.ForeignKey(Color, on_delete=models.CASCADE, null=True, blank=True, default=1)
    is_customizable = models.BooleanField(default=False)  # Only for products that can be customized
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    
    # Fixed price for all user-designed products
    price = models.DecimalField(max_digits=10, decimal_places=2, default=29.99)  # Fixed, non-editable

    class Meta:
        ordering = ['-date_added']

        indexes = [
            models.Index(fields=['-date_added'])
        ]

        #this Meta class making new products to be added in front or ascending order now every new product is added in the top. 


    def __str__(self):
        return self.name


class UserDesign(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Size = models.ForeignKey(Size, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    #product_image = models.ImageField(upload_to='designs/')
    shipping_address = models.TextField()
    crated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['crated_at']

        indexes = [
            models.Index(fields=['crated_at'])
        ]
    #same logic goes in but the opposite way since this one is custom_user model.

    def __str__(self):
        
        return self.shipping_address

 



# Cart model linked to the user
class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    #items = models.ManyToManyField(CartItem)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE, null=True, blank=True) #items works as a link between cart and cartitem model.
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, related_name='cartitems')
    quantity = models.PositiveIntegerField(default=0)
    #user_design = models.ForeignKey(UserDesigns, on_delete=models.CASCADE, null=True, blank=True)

# Order model
class Order(models.Model):
    
    
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed'),
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    pending_status = models.CharField(max_length=50, choices=PAYMENT_STATUS_CHOICES, default='PAYMENT_STATUS_PENDING')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    #address = models.CharField(max_length=300, blank=True, null=True),
    
    def __str__(self):
        return self.pending_status


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name = "items")
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    

    def __str__(self):
        return self.product.name