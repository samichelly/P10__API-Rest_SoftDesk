from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from projects import views


#  simplifier les path
router = routers.DefaultRouter()
# router.register(r"users", views.CustomUserViewSet)
router.register(r"projects", views.ProjectViewSet)
router.register(r"issues", views.IssueViewSet)
router.register(r"comments", views.CommentViewSet)

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("api/", include(router.urls)),

    # path("projects/", views.project_list, name="project-list"),
    # path(
    #     "api/projects/create/", views.ProjectCreateView.as_view(), name="project-create"
    # ),
    # path(
    #     "api/projects/<int:pk>/update/",
    #     views.ProjectUpdateView.as_view(),
    #     name="project-update",
    # ),
    # path("issues/", views.IssueListView.as_view(), name="issue-list"),
    # path("issues/create/", views.IssueCreateView.as_view(), name="issue-create"),
    # path("comments/", views.CommentViewSet.as_view(), name="comment-list"),
]

"""
urlpatterns = [
    path("projects/", views.ProjectListView.as_view(), name="project-list"),
    path("projects/create/", views.ProjectCreateView.as_view(), name="project-create"),
    path(
        "projects/<int:pk>/update/",
        views.ProjectUpdateView.as_view(),
        name="project-update",
    ),
    path(
        "projects/<int:pk>/delete/",
        views.ProjectDeleteView.as_view(),
        name="project-delete",
    ),
    path("issues/", views.IssueListView.as_view(), name="issue-list"),
    path("issues/create/", views.IssueCreateView.as_view(), name="issue-create"),
    path(
        "issues/<int:pk>/update/", views.IssueUpdateView.as_view(), name="issue-update"
    ),
    path(
        "issues/<int:pk>/delete/", views.IssueDeleteView.as_view(), name="issue-delete"
    ),
    path("comments/", views.CommentListView.as_view(), name="comment-list"),
    path("comments/create/", views.CommentCreateView.as_view(), name="comment-create"),
    path(
        "comments/<int:pk>/update/",
        views.CommentUpdateView.as_view(),
        name="comment-update",
    ),
    path(
        "comments/<int:pk>/delete/",
        views.CommentDeleteView.as_view(),
        name="comment-delete",
    ),
]
"""
urlpatterns += router.urls
