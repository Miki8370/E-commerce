from rest_framework import serializers
from . models import *


class CustomProductSerializer(serializers.ModelSerializer):
    class Meta:
        """
            fields = [
            'name',
            'description',
            'price',
            'image',
            'available_sizes',
            'available_colors',
            'is_customizable',
            'created_by'
            'date_added',
            'catagory',

        ]
        """
    
        fields = '__all__'
        
        model = CustomMadeProducts
