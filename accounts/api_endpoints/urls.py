from django.urls import path
from accounts.api_endpoints.Register.views import RegisterUserAPIView, RegisterConfirmAPIView
from accounts.api_endpoints.LoginSession.views import SessionLoginAPIView
from accounts.api_endpoints.LogoutSession.views import SessionLogoutAPIView
# Placeholder imports for other views (implement as needed)
# from accounts.api_endpoints.cart.views import (
#     CartItemsListAPIView, CartItemsCreateAPIView, CartItemsUpdateAPIView, CartItemsDeleteAPIView
# )
# from accounts.api_endpoints.profile.views import ProfileUpdateAPIView, ProfileDeleteAPIView
# from accounts.api_endpoints.password.views import PasswordResetRequestAPIView, PasswordResetConfirmAPIView
# from accounts.api_endpoints.saved.views import SavedProductsListAPIView, SaveProductAPIView
# from products.api_endpoints import UserReviewsListAPIView
# from accounts.template_views import RegisterView, LoginView, ProfileView

urlpatterns = [
    # Registration
    path("register/", RegisterUserAPIView.as_view(), name="register"),
    path("register/confirm/", RegisterConfirmAPIView.as_view(), name="register-confirm"),
    # Authentication
    path("login/", SessionLoginAPIView.as_view(), name="login-session"),
    path("logout/", SessionLogoutAPIView.as_view(), name="logout-session"),
    # Add other endpoints here as you implement them
]
