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
        title="Kunuz API",
        default_version='v1',
        description="API documentation for Kunuz Clone",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=[
        path('api/accounts/register/', RegisterUserAPIView.as_view(), name='register'),
        path('api/accounts/register/confirm/', RegisterConfirmAPIView.as_view(), name='register_confirm'),
        path('api/accounts/login/', SessionLoginAPIView.as_view(), name='session_login'),
        path('api/accounts/logout/', SessionLogoutAPIView.as_view(), name='session_logout'),
        path('api/token/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

        path('api/', include('news.api_endpoints.urls')),
    ]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.api_endpoints.urls')),
    path('api/', include('news.api_endpoints.urls')),
    path('api/token/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('i18n/', include('django.conf.urls.i18n')),
]
