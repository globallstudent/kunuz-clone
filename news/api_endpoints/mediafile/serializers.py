from rest_framework import serializers
from common.models import MediaFile

class MediaFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = '__all__'
