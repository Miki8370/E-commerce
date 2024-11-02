from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProduct(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=20.00, editable=False)
    image = models.ImageField(upload_to='products/')
    size = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    stack = models.IntegerField(default=0)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_design_orders')
    product = models.ForeignKey(UserProduct, on_delete=models.CASCADE)
    shipping_address = models.TextField()
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('shipped', 'Shipped'), ('delivered', 'Delivered')])
    date_ordered = models.DateTimeField(auto_now_add=True)
