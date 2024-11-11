from django.urls import path, include
from . views import *
from rest_framework.routers import DefaultRouter
from rest_framework import routers

router = routers.DefaultRouter()

router.register('products', ProductView, basename='products')
router.register('cart', CartView, basename='cart')
router.register('user_design', UserDesignView, basename='user_design')
router.register('catagory', CartView, basename='catagory')
router.register('UD_production', UDProductionView, basename='ud_productions')






urlpatterns = [
    path('', include(router.urls)),
    #path('user_design/', UserDesignView.as_view(), name='user_design'),
    #path("product/", ProductView.as_view(), name='product'),
    #path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    ##path("UD_prodcution/<int:pk>/", UDProductDeatailView.as_view(), name='ud_productions_detail'),
    #path('catagory/', CatagoryView.as_view(), name='catagory'),
    #path("catagory/<int:pk>/", CatgoryDetailView.as_view(), name="catagory_detail"),
    #path('cart/', CartView.as_view({'get': 'list', 'post': 'create',}), name='cart'),
    #path('cart/<uuid:pk>/', CartDetailView.as_view(), name='cart_detail'),
]