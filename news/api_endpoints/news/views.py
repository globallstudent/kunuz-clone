from rest_framework import generics, permissions
from news.models import News
from news.api_endpoints.news.serializers import NewsSerializer

class NewsListCreateAPIView(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class NewsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
