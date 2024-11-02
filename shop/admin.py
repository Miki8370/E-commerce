from django.contrib import admin
from . import models

# Register your models here.


admin.site.register(models.Products)
admin.site.register(models.Design)
admin.site.register(models.Cart)
admin.site.register(models.CartItem)
admin.site.register(models.Order)