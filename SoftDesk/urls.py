"""
URL configuration for SoftDesk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from users.views import SignupView
from projects import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # path("api/projects/", views.ProjectView.as_view(), name="project-list"),
    # path("api/projects/<int:pk>/", views.ProjectView.as_view(), name="project-detail"),
    # path("api/issues/", views.IssueView.as_view(), name="issue-list"),
    # path("api/issues/<int:pk>/", views.IssueView.as_view(), name="issue-detail"),
    # path("api/comments/", views.IssueView.as_view(), name="comment-list"),
    # path("api/comments/<int:pk>/", views.IssueView.as_view(), name="comment-detail"),


    # Vues pour les projets
    path('projects/', views.project_list, name='project-list'),
    path('projects/<int:project_pk>/', views.project_detail, name='project-detail'),
    
    # Vues pour les contributeurs
    path('projects/<int:project_pk>/contributors/', views.contributor_list, name='contributor-list'),
    path('projects/<int:project_pk>/contributors/<int:contributor_pk>/', views.contributor_detail, name='contributor-detail'),
    
    # Vues pour les problèmes (issues)
    path('projects/<int:project_pk>/issues/', views.issue_list, name='issue-list'),
    path('projects/<int:project_pk>/issues/<int:issue_pk>/', views.issue_detail, name='issue-detail'),
    
    # Vues pour les commentaires
    path('projects/<int:project_pk>/issues/<int:issue_pk>/comments/', views.comment_list, name='comment-list'),
    path('projects/<int:project_pk>/issues/<int:issue_pk>/comments/<int:comment_pk>/', views.comment_detail, name='comment-detail'),

]
