from django.contrib import admin
from common.models import MediaFile

@admin.register(MediaFile)
class MediaFileAdmin(admin.ModelAdmin):
    list_display = ("file", "media_type", "created_at", "updated_at")
    list_filter = ("media_type", "created_at")
    search_fields = ("file",)
    filter_horizontal = ("news",)
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        (None, {"fields": ("file", "media_type")}),
        ("Relations", {"fields": ("news",)}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )
