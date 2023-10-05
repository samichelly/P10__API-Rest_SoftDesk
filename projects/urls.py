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
    path("api/", include(router.urls)),
]

urlpatterns += router.urls
