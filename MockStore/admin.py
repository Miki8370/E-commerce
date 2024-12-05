from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Catagory)
class CatagoryAdmin(admin.ModelAdmin):
    pass



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
        'price',
        'catagory'
    ]


