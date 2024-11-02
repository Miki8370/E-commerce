from rest_framework import serializers
from . models import *


class UserDesignSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = UserProduct