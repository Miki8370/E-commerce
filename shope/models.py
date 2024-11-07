"""from django.db import models
from django.contrib.auth.models import User
# Create your models here.

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
    
    # Fixed price for all user-designed products
    price = models.DecimalField(max_digits=10, decimal_places=2, default=29.99)  # Fixed, non-editable

    def __str__(self):
        return f"{self.user.username}'s design on {self.product.name}"


class UserDesign(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Size = models.ForeignKey(Size, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='designs/')
    shipping_address = models.TextField()
    crated_at = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.user

"""