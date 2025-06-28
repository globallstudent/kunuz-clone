from django.contrib import admin
from news.models import News, Category, Tag, Comment

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "is_active", "view_count", "created_at")
    list_filter = ("is_active", "categories", "tags", "author")
    search_fields = ("title", "content", "author__email")
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("categories", "tags", "liked_by")
    date_hierarchy = "created_at"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created_at")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created_at")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("news", "user", "content", "created_at")
    search_fields = ("news__title", "user__email", "content")
    list_filter = ("news", "user")
