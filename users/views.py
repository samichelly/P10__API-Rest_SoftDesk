from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import CustomUser
from projects.models import Project, Contributor, Issue, Comment
from .serializers import SignupSerializer, CustomUserSerializer


class SignupView(generics.CreateAPIView):
    """
    View for user signup.
    """

    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = SignupSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def users_list(request):
    """
    Get the list of users who share their data.
    """
    # if request.user:
    queryset = CustomUser.objects.all().filter(can_data_be_shared=True)
    current_user = CustomUser.objects.get(pk=request.user.id)
    queryset |= CustomUser.objects.filter(pk=current_user.id)
    serializer = CustomUserSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    # else:
    #     return Response("Protected data", status=status.HTTP_403_FORBIDDEN)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def user_detail(request, user_pk):
    """
    Retrieve, update, or delete a user's profile.
    """
    user = get_object_or_404(CustomUser, id=user_pk)

    if (request.user != user) and (request.user.is_superuser is False):
        return Response(
            "Access denied.",
            status=status.HTTP_403_FORBIDDEN,
        )

    if request.method == "GET":
        serializer = CustomUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = CustomUserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        print("test")
        projects_to_reassign = Project.objects.filter(author=user)
        issues_to_reassign = Issue.objects.filter(author=user)
        print("projects_to_reassign")
        print(projects_to_reassign)
        print("issues_to_reassign")
        print(issues_to_reassign)
        new_author = None
        new_issue_author = False

        for project in projects_to_reassign:
            new_author = Contributor.objects.filter(
                project=project, role="CONTRIBUTOR"
            ).first()
            print("new_author")
            print(new_author)
            if new_author:
                new_author.role = "AUTHOR"
                new_author.save()
                project.author = new_author.user
                project.save()

        for issue in issues_to_reassign:
            print("issue1")
            # print(new_author)
            if issue.project.author != user:
                issue.author = issue.project.author
                new_issue_author = True
                issue.save()
            else:
                if new_author:
                    print("issue2")
                    issue.author = new_author.user
                    issue.save()

        if new_author or new_issue_author:
            print("gomme")
            user.date_of_birth = None
            user.can_be_contacted = False
            user.can_data_be_shared = False
            user.is_active = False
            user.save()
            print("gomme OK")
            return Response(
                "Profile soft deleted, new author assigned",
                status=status.HTTP_204_NO_CONTENT,
            )
        else:
            return Response(
                "You must define a new contributor before deleting the user",
                status=status.HTTP_400_BAD_REQUEST,
            )


"""
    elif request.method == "DELETE":
        try:
            projects_to_reassign = Project.objects.filter(author=user)
            for project in projects_to_reassign:
                new_author = Contributor.objects.filter(
                    project=project, role="CONTRIBUTOR"
                ).first()

                if new_author:
                    new_author.role = "AUTHOR"
                    new_author.save()

                    project.author = new_author.user
                    project.save()
        try:
            issues_to_reassign = Issue.objects.filter(author=user)
                issue.author = new_author.user
                project.save()

            # finally
                user.username = "data unavailable"
                user.email = "data unavailable"
                user.date_of_birth = None
                user.can_be_contacted = False
                user.can_data_be_shared = False
                user.save()
                return Response(
                    "Profile soft deleted, new author assigned",
                    status=status.HTTP_204_NO_CONTENT,
                )

            else:
                return Response(
                    "You must define a new contributor before deleting the user",
                    status=status.HTTP_400_BAD_REQUEST,
                )

        # ajouter un user temporaire
        # ajouter la possibilité d'etre supp par un admin
        # garder un trace de l'utilisateur

        """
