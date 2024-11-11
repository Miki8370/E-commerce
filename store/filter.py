from django_filters.rest_framework import FilterSet
from store.models import Product


class ProductFilter(FilterSet):
    class Meta: #used to filter product model with catagory, and name
        model = Product
        fields = ['category', 'name']


