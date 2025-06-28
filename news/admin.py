from django.contrib import admin
from news.models import News, Category, Tag, Comment

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "is_active", "view_count", "publish_at", "created_at")
    list_filter = ("is_active", "categories", "tags", "author", "publish_at")
    search_fields = ("title", "content", "author__email")
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("categories", "tags", "liked_by")
    date_hierarchy = "publish_at"
    readonly_fields = ("view_count", "created_at", "updated_at")
    fieldsets = (
        (None, {
            'fields': ("title", "slug", "content", "author", "default_image")
        }),
        ("Relations", {
            'fields': ("categories", "tags", "liked_by")
        }),
        ("Status & Scheduling", {
            'fields': ("is_active", "publish_at", "view_count")
        }),
        ("Timestamps", {
            'fields': ("created_at", "updated_at")
        }),
    )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created_at", "updated_at")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ("created_at", "updated_at")
    ordering = ("-created_at",)
    fieldsets = (
        (None, {"fields": ("name", "slug")}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created_at", "updated_at")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ("created_at", "updated_at")
    ordering = ("-created_at",)
    fieldsets = (
        (None, {"fields": ("name", "slug")}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("news", "user", "content", "created_at", "updated_at")
    search_fields = ("news__title", "user__email", "content")
    list_filter = ("news", "user", "created_at")
    readonly_fields = ("created_at", "updated_at")
    ordering = ("-created_at",)
    fieldsets = (
        (None, {"fields": ("news", "user", "content")}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )
