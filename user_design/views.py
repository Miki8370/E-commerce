from django.shortcuts import render
from . serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from . models import *
# Create your views here.


class DesignView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserDesignSerializer


    

    def post(self, request):
        serializer = UserDesignSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
