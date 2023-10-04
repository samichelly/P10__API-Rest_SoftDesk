from rest_framework import serializers
from .models import CustomUser, Project


# from .models import Issue, Comment


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        # fields = "__all__"

        fields = [
            "id",
            "author",
            "title",
            #     "description",
            #     "project_type",
            #     "created_time",
            #     "contributors",  # Ajoutez le champ des contributeurs
        ]


"""


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = [
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
        ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "issue", "author", "description", "created_time"]
"""
