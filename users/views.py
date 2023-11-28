from rest_framework import views, generics, viewsets
from rest_framework.status import HTTP_201_CREATED
from rest_framework.exceptions import ParseError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import *
from .models import *


class LoginView(views.APIView):
    def post(self, request):
        pass


class CreateAccountViewset(viewsets.ModelViewSet):
    queryset = KnowerUser.objects.all()
    serializer_class = CreateAccountSerializer
    permission_classes = [AllowAny]
