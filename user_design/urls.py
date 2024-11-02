from django.urls import path
from . views import *

urlpatterns = [

    path('design/', DesignView.as_view(), name='design'),


]