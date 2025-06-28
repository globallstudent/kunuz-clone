from django.urls import path
from news.api_endpoints.news.views import NewsListCreateAPIView, NewsRetrieveUpdateDestroyAPIView
from news.api_endpoints.category.views import CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView
from news.api_endpoints.tag.views import TagListCreateAPIView, TagRetrieveUpdateDestroyAPIView
from news.api_endpoints.comment.views import CommentListCreateAPIView, CommentRetrieveUpdateDestroyAPIView
from news.api_endpoints.mediafile.views import MediaFileListCreateAPIView, MediaFileRetrieveUpdateDestroyAPIView

urlpatterns = [
    # News
    path('news/', NewsListCreateAPIView.as_view(), name='news-list-create'),
    path('news/<int:pk>/', NewsRetrieveUpdateDestroyAPIView.as_view(), name='news-detail'),
    # Category
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail'),
    # Tag
    path('tags/', TagListCreateAPIView.as_view(), name='tag-list-create'),
    path('tags/<int:pk>/', TagRetrieveUpdateDestroyAPIView.as_view(), name='tag-detail'),
    # Comment
    path('comments/', CommentListCreateAPIView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view(), name='comment-detail'),
    # MediaFile
    path('mediafiles/', MediaFileListCreateAPIView.as_view(), name='mediafile-list-create'),
    path('mediafiles/<int:pk>/', MediaFileRetrieveUpdateDestroyAPIView.as_view(), name='mediafile-detail'),
]
