from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserViews
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView  #import access and refresh tokens

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/register/', CreateUserViews.as_view(), name='register'),
    path('api/token', TokenObtainPairView.as_view(), name ='get_token'),
    path('api/refresh', TokenRefreshView.as_view(), name ='refresh'),
    path('api-auth/', include('rest_framework.urls'))
]
