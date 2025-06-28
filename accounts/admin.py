from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("email", "first_name", "last_name", "is_active", "is_staff", "is_superuser", "is_confirmed", "last_login", "created_at")
    search_fields = ("email", "first_name", "last_name", "bio")
    list_filter = ("is_active", "is_staff", "is_superuser", "is_confirmed")
    ordering = ("-created_at",)
    readonly_fields = ("last_login", "created_at", "updated_at")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "avatar", "bio")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "is_confirmed", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "created_at", "updated_at")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "is_active", "is_staff", "is_superuser", "is_confirmed")
        }),
    )
