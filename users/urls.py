from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import SignupView, LoginView

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    # path("login/", LoginView.as_view()),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
]
