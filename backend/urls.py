from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/v1/', include('shop.urls')),
    path('api/v2/', include('user_design.urls')),
    path('api/v3/', include('custom_product.urls')),
    # path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),  # No namespace here
    path("dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),  # No namespace here
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('accounts/', include('allauth.urls')),


]
