from django.urls import path, include
from rest_framework.routers import DefaultRouter
from custom_product.views import *
from store.views import *
from user_design.views import *
from rest_framework_nested.routers import NestedDefaultRouter

router = DefaultRouter()

#custom_product urls
router.register('custom-made-products', CustomProductsView, basename='c-products')

#store urls
router.register('user-made-products', ProductView, basename='products')
router.register('add-designs', UserDesignView, basename='user_design')
router.register('catagory', CatagoryView, basename='catagory')
router.register('view-designs', UDProductionView, basename='ud_productions')
router.register('all-design', AllDesignAdminView, basename='design-for-admins')
router.register('orders', OrderView, basename='order')
router.register('carts', CartView, basename='cart')

cart_router = NestedDefaultRouter(router, 'carts', lookup='cart')
cart_router.register("items", CartItemView, basename="cart-items")

#user_design urls
router.register('design', DesignViewSet, basename='design')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(cart_router.urls)),
]