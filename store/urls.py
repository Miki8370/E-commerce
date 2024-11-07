from django.urls import path
from . views import *

urlpatterns = [
    path('user_design/', UserDesignView.as_view(), name='user_design'),
    path("product/", ProductView.as_view(), name='product'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path("UD_prodcution/", UDProductionView.as_view(), name="ud_productions"),
    path("UD_prodcution/<int:pk>/", UDProductDeatailView.as_view(), name='ud_productions_detail'),
    path('catagory/', CatagoryView.as_view(), name='catagory'),
    path("catagory/<int:pk>/", CatgoryDetailView.as_view(), name="catagory_detail"),

]