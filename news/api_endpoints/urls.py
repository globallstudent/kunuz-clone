from rest_framework.routers import DefaultRouter
from .views import NewsViewSet, CategoryViewSet, TagViewSet, CommentViewSet, MediaFileViewSet

router = DefaultRouter()
router.register(r'news', NewsViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'tags', TagViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'mediafiles', MediaFileViewSet)

urlpatterns = router.urls
