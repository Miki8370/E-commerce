from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.ProductSerializerView.as_view(), name='product'),
    
]