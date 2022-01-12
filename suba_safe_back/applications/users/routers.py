# Third-Party Apps Imports
from rest_framework.routers import DefaultRouter

from . import viewsets


router = DefaultRouter()

router.register(r'usuarios', viewsets.UserViewSet, basename='usuarios')

urlpatterns = router.urls

