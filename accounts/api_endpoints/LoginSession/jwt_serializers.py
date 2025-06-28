from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from accounts.models import User

class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = User.USERNAME_FIELD

    def validate(self, attrs):
        # Accept email instead of username
        email = attrs.get('email')
        password = attrs.get('password')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError('No user with this email.')
        if not user.check_password(password):
            raise serializers.ValidationError('Incorrect password.')
        if not user.is_confirmed:
            raise serializers.ValidationError('Email not confirmed.')
        data = super().validate({'username': email, 'password': password})
        return data

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token
