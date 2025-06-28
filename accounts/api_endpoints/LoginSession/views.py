# loginsession
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import serializers
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema


class SessionLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class SessionLoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(request_body=SessionLoginSerializer)
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return JsonResponse(
                {"error": "Email and password are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"message": "Login successful"})
        else:
            return JsonResponse(
                {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )


__all__ = ["SessionLoginAPIView"]
