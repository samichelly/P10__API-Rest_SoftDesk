from django.conf import settings
from django.db import models
import uuid


TYPE = [
    ("BACKEND", "BACKEND"),
    ("FRONTEND", "FRONTEND"),
    ("iOS", "iOS"),
    ("ANDROID", "ANDROID"),
]

ROLE = [("AUTHOR", "AUTHOR"), ("CONTRIBUTOR", "CONTRIBUTOR")]

PRIORITY = [("LOW", "LOW"), ("MEDIUM", "MEDIUM"), ("HIGH", "HIGH")]

TAG = [("BUG", "BUG"), ("TASK", "TASK"), ("UPGRADE", "UPGRADE")]

STATUS = [("TODO", "TODO"), ("IN PROGRESS", "IN PROGRESS"), ("DONE", "DONE")]


class Project(models.Model):
    title = models.CharField(max_length=128)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="author"
    )
    description = models.TextField(max_length=2048)
    type = models.CharField(choices=TYPE, max_length=8)
    created_time = models.DateTimeField(auto_now_add=True)


class Contributor(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(
        to=Project, on_delete=models.CASCADE, related_name="contributors"
    )
    role = models.CharField(max_length=11, choices=ROLE, default="CONTRIBUTOR")


class Issue(models.Model):
    title = models.CharField(max_length=128)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(to=Contributor, on_delete=models.CASCADE)
    description = models.TextField(max_length=2048)
    tag = models.CharField(choices=TAG, max_length=7)
    priority = models.CharField(choices=PRIORITY, max_length=6, default="LOW")
    status = models.CharField(choices=STATUS, max_length=11, default="TODO")
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    issue = models.ForeignKey(to=Issue, on_delete=models.CASCADE)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(max_length=2048)
    id_comment = models.UUIDField(default=uuid.uuid4, editable=False)
    created_time = models.DateTimeField(auto_now_add=True)
