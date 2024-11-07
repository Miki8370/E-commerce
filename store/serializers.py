from rest_framework import serializers
from . models import *


class UserDesignSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = UserDesign


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Product
        



class CatagorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Catagory
