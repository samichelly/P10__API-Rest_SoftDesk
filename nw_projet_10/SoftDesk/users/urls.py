from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import SignupView, LoginView

urlpatterns = [
    # Remarquez que j'ai changé le nom 'signup' en 'user-signup' pour plus de clarté
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
]
