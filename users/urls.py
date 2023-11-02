from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup/", views.SignupView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
    path("profile/", views.users_list),
    path("profile/<int:user_pk>/", views.user_detail),
]
