"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from accounts.api_endpoints.LoginSession.jwt_views import EmailTokenObtainPairView
from accounts.api_endpoints.Register.views import RegisterUserAPIView, RegisterConfirmAPIView
from accounts.api_endpoints.LoginSession.views import SessionLoginAPIView
from accounts.api_endpoints.LogoutSession.views import SessionLogoutAPIView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf.urls.i18n import i18n_patterns

schema_view = get_schema_view(
    openapi.Info(
        title="Kunuz Clone API",
        default_version='v1',
        description="API documentation for Kunuz Clone",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterUserAPIView.as_view(), name='register'),
    path('api/register/confirm/', RegisterConfirmAPIView.as_view(), name='register_confirm'),
    path('api/session/login/', SessionLoginAPIView.as_view(), name='session_login'),
    path('api/session/logout/', SessionLogoutAPIView.as_view(), name='session_logout'),
    path('api/', include('news.api_endpoints.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += [
    path('i18n/', include('django.conf.urls.i18n')),
]
