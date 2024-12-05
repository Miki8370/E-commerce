from django.contrib import admin
from . models import *
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
    #list_filter = ['available_colors']



admin.site.register(Color)
admin.site.register(Size)
admin.site.register(UserDesign)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(Catagory)
admin.site.register(Order)
admin.site.register(OrderItem)

