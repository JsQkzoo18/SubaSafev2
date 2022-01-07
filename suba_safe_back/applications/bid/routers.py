from rest_framework.routers import DefaultRouter

from . import viewsets


router = DefaultRouter()

router.register(r'ofertas', viewsets.BidProcessViewSet, basename='ofertas')

urlpatterns = router.urls