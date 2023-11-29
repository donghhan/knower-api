from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from django.urls import path
from . import views

router = routers.SimpleRouter()
router.register(r"create-account", views.CreateAccountViewset)
router.register(r"login", views.LoginView)

tokenview = [
    path("token", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify", jwt_views.TokenVerifyView.as_view(), name="token_verify"),
]

urlpatterns = router.urls + tokenview
