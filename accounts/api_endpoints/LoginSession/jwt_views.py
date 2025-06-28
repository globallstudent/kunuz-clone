from rest_framework_simplejwt.views import TokenObtainPairView
from .jwt_serializers import EmailTokenObtainPairSerializer

class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer
