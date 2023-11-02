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
        "can_be_contacted",
        "can_data_be_shared",
        "password",
        # "custom_is_superuser",
    )


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "author",
        "title",
        "description",
        # "project_type",
        # "created_time",
        # "contributors",
    )


class ContributorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "project",
        "user",
        "role",
        # "contributed_projects",
    )


class IssueAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "project",
        "author",
        # "assigned_to",
        "title",
        # "description",
        "priority",
        "tag",
        "status",
        "created_time",
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "issue",
        "author",
        "description",
        # "project_type",
        "created_time",
        # "id_comment",
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(Comment, CommentAdmin)
