from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupSerializer
from django.urls import reverse
from rest_framework_simplejwt.views import TokenObtainPairView

CustomUser = get_user_model()


class SignupView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = SignupSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect("/login/")

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
