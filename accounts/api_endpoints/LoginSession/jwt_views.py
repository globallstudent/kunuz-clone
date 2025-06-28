from rest_framework_simplejwt.views import TokenObtainPairView
from .jwt_serializers import EmailTokenObtainPairSerializer
from rest_framework import permissions

class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer
    permission_classes = [permissions.AllowAny]
