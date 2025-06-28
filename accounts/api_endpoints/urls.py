from django.urls import path
from accounts.api_endpoints.Register.views import RegisterUserAPIView, RegisterConfirmAPIView
from accounts.api_endpoints.LoginSession.views import SessionLoginAPIView
from accounts.api_endpoints.LogoutSession.views import SessionLogoutAPIView

urlpatterns = [
    # Registration
    path("register/", RegisterUserAPIView.as_view(), name="register"),
    path("register/confirm/", RegisterConfirmAPIView.as_view(), name="register-confirm"),
    # Authentication
    path("login/", SessionLoginAPIView.as_view(), name="login-session"),
    path("logout/", SessionLogoutAPIView.as_view(), name="logout-session"),
    
]
