from django.urls import path
from . views import *


urlpatterns = [
    path("product/", CustomProductView.as_view(), name='custom_products'),

]