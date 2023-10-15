from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from projects import views


#  simplifier les path
# router = routers.DefaultRouter()
# router.register(r"users", views.CustomUserViewSet)
# router.register(r"projects", views.ProjectView)
# router.register(r"issues", views.IssueView)
# router.register(r"comments", views.CommentView)

urlpatterns = [
    # path("api/", include(router.urls)),
    # path("api/projects/", views.ProjectView.as_view(), name="project-list"),
    # path("api/projects/<int:pk>/", views.ProjectView.as_view(), name="project-detail"),
    # path("api/issues/", views.IssueView.as_view(), name="issue-list"),
    # path("api/issues/<int:pk>/", views.IssueView.as_view(), name="issue-detail"),
    # path("api/comments/", views.IssueView.as_view(), name="comment-list"),
    # path("api/comments/<int:pk>/", views.IssueView.as_view(), name="comment-detail"),
]

# urlpatterns += router.urls
