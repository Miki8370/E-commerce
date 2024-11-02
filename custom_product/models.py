from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Catagory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    



class CustomMadeProducts(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    available_sizes = models.CharField(max_length=100)  # "S, M, L, XL"
    available_colors = models.CharField(max_length=100)  # "Red, Blue, Black"
    is_customizable = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name
    

