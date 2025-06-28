from rest_framework import generics, permissions
from common.models import MediaFile
from news.api_endpoints.mediafile.serializers import MediaFileSerializer

class MediaFileListCreateAPIView(generics.ListCreateAPIView):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class MediaFileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
