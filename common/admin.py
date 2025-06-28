from django.contrib import admin
from common.models import MediaFile

@admin.register(MediaFile)
class MediaFileAdmin(admin.ModelAdmin):
    list_display = ("file", "media_type", "created_at")
    list_filter = ("media_type",)
    search_fields = ("file",)
    filter_horizontal = ("news",)
