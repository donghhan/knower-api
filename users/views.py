from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from rest_framework import views, generics, viewsets
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.exceptions import ParseError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenRefreshSerializer,
)
from .serializers import *
from .models import KnowerUser


class LoginView(viewsets.ViewSet):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer
    queryset = KnowerUser.objects.all()

    def create(self, request):
        email = request.data["email"]
        password = request.data["password"]

        user = KnowerUser.objects.get(email=email)


class CreateAccountViewset(viewsets.ModelViewSet):
    queryset = KnowerUser.objects.all()
    serializer_class = CreateAccountSerializer
    permission_classes = [AllowAny]
