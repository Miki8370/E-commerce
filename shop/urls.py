"""
from django.urls import path, include
from . import views
#from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('product_/', views.ProductView.as_view(), name="product2"),
    path('design_/', views.DesignView.as_view(), name="design2"),
    path('product/', views.ProductSerializerView.as_view(), name='product'),
    path('Design/', views.DesignSerializerView.as_view(), name='design'),
    path('cart/', views.CartSerializerView.as_view(), name='cart'),
    path('cart-item/', views.CartItemSerializerView.as_view(), name='cart_item'),
    path('order/', views.OrderSerializerView.as_view(), name='order'),
    


]
"""