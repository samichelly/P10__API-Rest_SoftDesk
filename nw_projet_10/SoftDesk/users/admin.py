from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "date_of_birth",
        "can_be_contacted",
        "can_data_be_shared",
        "password",
    )
    list_filter = ("date_of_birth", "can_be_contacted", "can_data_be_shared")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Personal info",
            {
                "fields": (
                    "email",
                    "date_of_birth",
                    "can_be_contacted",
                    "can_data_be_shared",
                )
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
