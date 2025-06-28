from django.db import models
from common.models import BaseModel

class News(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)

    author = models.ForeignKey(
        'accounts.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='news'
    )

    categories = models.ManyToManyField(
        'news.Category',
        related_name='news',
        blank=True
    )

    tags = models.ManyToManyField(
        'news.Tag',
        related_name='news',
        blank=True
    )

    default_image = models.ImageField(
        upload_to='news/images/',
        null=True,
        blank=True
    )

    is_active = models.BooleanField(default=True)
    view_count = models.PositiveIntegerField(default=0)
    publish_at = models.DateTimeField(null=True, blank=True, help_text="Schedule news to be published at this time.")

    liked_by = models.ManyToManyField(
        'accounts.User',
        blank=True,
        related_name='liked_news'
    )

    def __str__(self):
        return self.title


class Category(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name_plural = "Categories"


class Tag(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name_plural = "Tags"


class Comment(BaseModel):
    content = models.TextField(null=True, blank=True)

    user = models.ForeignKey(
        'accounts.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='comments'
    )

    news = models.ForeignKey(
        'news.News',
        on_delete=models.CASCADE,
        related_name='comments'
    )

    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='replies'
    )

    def __str__(self):
        return f"Comment by {self.user} on {self.news}"
