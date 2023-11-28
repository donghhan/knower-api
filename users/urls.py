from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r"create-account", views.CreateAccountViewset)

urlpatterns = router.urls
