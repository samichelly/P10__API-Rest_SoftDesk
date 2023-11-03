from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from projects.models import Project, Contributor, Issue, Comment


class CustomUserAdmin(UserAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
        "date_of_birth",
        "is_superuser",
        "is_active",
        "can_be_contacted",
        "can_data_be_shared",
        "password",
    )


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "author",
        "title",
        "description",
    )


class ContributorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "project",
        "user",
        "role",
    )


class IssueAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "project",
        "author",
        "assigned_to",
        "title",
        "description",
        "priority",
        "tag",
        "status",
        "created_time",
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "issue",
        "author",
        "description",
        "id_comment",
        "created_time",
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(Comment, CommentAdmin)
