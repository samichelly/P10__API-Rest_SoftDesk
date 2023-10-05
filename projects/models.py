from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


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


# project - Contributor -> ManyToMany
class Project(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=2000)
    project_type = models.CharField(choices=TYPE, max_length=200)
    created_time = models.DateTimeField(auto_now_add=True)
    contributors = models.ManyToManyField(
        CustomUser, through="Contributor", related_name="contributed_projects"
    )


class Contributor(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    role = models.CharField(choices=ROLE, max_length=200)


class Issue(models.Model):
    # Relation ManyToOne betwween Project and Issue

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="contributor_issue"
    )
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    priority = models.CharField(choices=PRIORITY, max_length=200)
    tag = models.CharField(choices=TAG, max_length=200)
    status = models.CharField(choices=STATUS, default="TO DO", max_length=200)
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    # Relation ManyToOne between Issue and Comment
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.TextField(max_length=2048)
    # id_comment = models.UUIDField(auto_created=True)
    created_time = models.DateTimeField(auto_now_add=True)
