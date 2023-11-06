from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users.models import CustomUser

from .models import Project, Issue, Contributor, Comment
from .permissions import (
    ProjectPermissions,
    ContributorPermissions,
    IssuePermissions,
    CommentPermissions,
)
from .serializers import (
    ProjectSerializer,
    IssueSerializer,
    CommentSerializer,
    ContributorSerializer,
)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated, ProjectPermissions])
def project_list(request):
    """
    List and create projects.
    - GET: Lists projects for which the user is a contributor.
    - POST: Creates a new project with the current user as the author.
    """
    if request.method == "GET":
        # List projects for which the user is a contributor.
        projects = Project.objects.filter(contributors__user=request.user)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        # Create a new project with the current user as the author.
        data = request.data.copy()
        data["author"] = request.user.id

        serializer = ProjectSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            project = serializer.save()
            Contributor.objects.create(
                user=request.user, project=project, role="AUTHOR"
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated, ProjectPermissions])
def project_detail(request, project_pk):
    """
    Retrieve, update, or delete a specific project.
    - GET: Retrieves project details.
    - PUT: Updates project details.
    - DELETE: Deletes the project.
    """
    project = get_object_or_404(Project, id=project_pk)

    if request.method == "GET":
        # Retrieve project details.
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        # Update project details.
        data = request.data.copy()
        data["author"] = project.author.id

        serializer = ProjectSerializer(project, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        # Delete the project.
        project.delete()
        return Response(
            "Project successfully deleted.", status=status.HTTP_204_NO_CONTENT
        )


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated, ContributorPermissions])
def contributor_list(request, project_pk):
    """
    List contributors within a project and add new contributors.
    - GET: Lists contributors within a project.
    - POST: Adds a new contributor to the project.
    """
    project = get_object_or_404(Project, id=project_pk)

    if request.method == "GET":
        # List contributors within the project.
        contributors = Contributor.objects.filter(project=project)
        serializer = ContributorSerializer(contributors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        # Add a new contributor to the project.
        data = request.data.copy()
        data["project"] = project.id

        try:
            Contributor.objects.get(user=data["user"], project=project.id)
            return Response(
                "This user has already been added.", status=status.HTTP_400_BAD_REQUEST
            )
        except Contributor.DoesNotExist:
            try:
                CustomUser.objects.get(id=data["user"])
                serializer = ContributorSerializer(data=data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            except CustomUser.DoesNotExist:
                return Response(
                    "This user does not exist.", status=status.HTTP_400_BAD_REQUEST
                )


@api_view(["DELETE"])
@permission_classes([IsAuthenticated, ContributorPermissions])
def contributor_detail(request, project_pk, contributor_pk):
    """
    Delete a contributor within a project.
    - DELETE: Deletes a contributor within a project.
    """
    get_object_or_404(Project, id=project_pk)
    contributor = get_object_or_404(Contributor, id=contributor_pk)

    if request.method == "DELETE":
        if contributor.role == "AUTHOR":
            return Response(
                "Project author cannot be deleted.", status=status.HTTP_400_BAD_REQUEST
            )
        else:
            contributor.delete()
            return Response(
                "Contributor successfully deleted.", status=status.HTTP_204_NO_CONTENT
            )


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated, IssuePermissions])
def issue_list(request, project_pk):
    """
    List and create issues within a project.
    - GET: Lists issues within a project.
    - POST: Creates a new issue within the project.
    """
    project = get_object_or_404(Project, id=project_pk)

    if request.method == "GET":
        # List issues within the project.
        issues = Issue.objects.filter(project=project)
        serializer = IssueSerializer(issues, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        # Create a new issue within the project.
        data = request.data.copy()
        data["project"] = project.id
        data["author"] = request.user.id

        try:
            Contributor.objects.get(id=data["assigned_to"], project=project.id)
            serializer = IssueSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Contributor.DoesNotExist:
            return Response(
                "This user is not contributing to this project or does not exist.",
                status=status.HTTP_400_BAD_REQUEST,
            )


@api_view(["PUT", "DELETE"])
@permission_classes([IsAuthenticated, IssuePermissions])
def issue_detail(request, project_pk, issue_pk):
    """
    Retrieve, update, or delete a specific issue within a project.
    - PUT: Updates issue details.
    - DELETE: Deletes the issue.
    """
    project = get_object_or_404(Project, id=project_pk)
    issue = get_object_or_404(Issue, id=issue_pk)

    if request.method == "PUT":
        # Update issue details.
        data = request.data.copy()
        data["project"] = project.id
        data["author"] = issue.author.id

        try:
            Contributor.objects.get(id=data["assigned_to"], project=project.id)
            serializer = IssueSerializer(issue, data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Contributor.DoesNotExist:
            return Response(
                "This user is not contributing to this project or does not exist.",
                status=status.HTTP_400_BAD_REQUEST,
            )

    elif request.method == "DELETE":
        # Delete the issue.
        issue.delete()
        return Response(
            "Issue successfully deleted.", status=status.HTTP_204_NO_CONTENT
        )


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated, CommentPermissions])
def comment_list(request, project_pk, issue_pk):
    """
    List and create comments within an issue.
    - GET: Lists comments within an issue.
    - POST: Adds a new comment to the issue.
    """
    get_object_or_404(Project, id=project_pk)
    issue = get_object_or_404(Issue, id=issue_pk)

    if request.method == "GET":
        # List comments within the issue.
        comments = Comment.objects.filter(issue=issue)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        # Add a new comment to the issue.
        data = request.data.copy()
        data["issue"] = issue.id
        data["author"] = request.user.id

        serializer = CommentSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated, CommentPermissions])
def comment_detail(request, project_pk, issue_pk, comment_pk):
    """
    Retrieve, update, or delete a specific comment within an issue.
    - GET: Retrieves comment details.
    - PUT: Updates comment details.
    - DELETE: Deletes the comment.
    """
    get_object_or_404(Project, id=project_pk)
    issue = get_object_or_404(Issue, id=issue_pk)
    comment = get_object_or_404(Comment, id=comment_pk)

    if request.method == "GET":
        # Retrieve comment details.
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        # Update comment details.
        data = request.data.copy()
        data["issue"] = issue.id
        data["author"] = comment.author.id

        serializer = CommentSerializer(comment, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        # Delete the comment.
        comment.delete()
        return Response(
            "Comment successfully deleted.", status=status.HTTP_204_NO_CONTENT
        )
