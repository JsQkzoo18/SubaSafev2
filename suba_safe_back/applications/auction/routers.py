# Third-Party Apps Imports
from rest_framework.routers import DefaultRouter

# ViewSets Imports
from . import viewsets

# Registro de rutas para ViewSet de Subasta
router = DefaultRouter()
router.register(r'subastas', viewsets.AuctionProcessViewSet, basename='subastas')
urlpatterns = router.urls