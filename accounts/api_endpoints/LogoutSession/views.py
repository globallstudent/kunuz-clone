# logoutsession
from django.contrib.auth import logout
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import permissions


class SessionLogoutAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        logout(request)
        return JsonResponse({"message": "Logout successful"})


__all__ = ["SessionLogoutAPIView"]
