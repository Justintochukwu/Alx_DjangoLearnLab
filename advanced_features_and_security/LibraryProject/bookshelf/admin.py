from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.utils.translation import gettext_lazy as _


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Fields to show in the user list
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "date_of_birth")

    # Fields to filter by in the list
    list_filter = ("is_staff", "is_superuser", "is_active")

    # Fieldsets for the user edit form
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "date_of_birth", "profile_photo")}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    # Fields shown when creating a new user from the admin
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "date_of_birth", "profile_photo"),
        }),
    )

    search_fields = ("username", "email")
    ordering = ("username",)


# Register the custom user admin
admin.site.register(CustomUser, CustomUserAdmin)
