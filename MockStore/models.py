from django.db import models

# Create your models here.


class Catagory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=3)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

    
