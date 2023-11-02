from rest_framework import permissions
from rest_framework.generics import get_object_or_404

from .models import Project, Issue, Comment


class ProjectPermissions(permissions.BasePermission):
    """
    Permissions for project-related actions.
    - Users can view projects if they are contributors.
    - Only the project author can modify the project.
    - No specific project is required for some views (e.g., project list).
    """

    def has_permission(self, request, view):
        try:
            project = get_object_or_404(Project, id=view.kwargs["project_pk"])
            if request.method in permissions.SAFE_METHODS:
                return project in Project.objects.filter(
                    contributors__user=request.user
                )
            return request.user == project.author
        except KeyError:
            return True


class ContributorPermissions(permissions.BasePermission):
    """
    Permissions for contributors within a project.
    - Contributors can view contributors of a project.
    - Contributors can modify their own contributor record within a project.
    - No specific project is required for some views (e.g., contributor list).
    """

    def has_permission(self, request, view):
        project = get_object_or_404(Project, id=view.kwargs["project_pk"])
        if request.method in permissions.SAFE_METHODS:
            return project in Project.objects.filter(contributors__user=request.user)
        return request.user == project.author


class IssuePermissions(permissions.BasePermission):
    """
    Permissions for issue-related actions within a project.
    - Users can view issues if they are contributors to the project.
    - Only the author of an issue can modify the issue.
    - No specific issue or project is required for some views (e.g., issue list).
    """

    def has_permission(self, request, view):
        project = get_object_or_404(Project, id=view.kwargs["project_pk"])
        try:
            issue = get_object_or_404(Issue, id=view.kwargs["issue_pk"])
            return request.user == issue.author
        except KeyError:
            return project in Project.objects.filter(contributors__user=request.user)


class CommentPermissions(permissions.BasePermission):
    """
    Permissions for comments on issues within a project.
    - Users can view comments if they are contributors to the project.
    - Only the author of a comment can modify the comment.
    - No specific comment, issue, or project is required for some views (e.g., comment list).
    """

    def has_permission(self, request, view):
        project = get_object_or_404(Project, id=view.kwargs["project_pk"])
        try:
            comment = get_object_or_404(Comment, id=view.kwargs["comment_pk"])
            if request.method in permissions.SAFE_METHODS:
                return project in Project.objects.filter(
                    contributors__user=request.user
                )
            return request.user == comment.author
        except KeyError:
            return project in Project.objects.filter(contributors__user=request.user)
