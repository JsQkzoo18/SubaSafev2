from rest_framework.routers import DefaultRouter

from . import viewsets


router = DefaultRouter()

router.register(r'categorias', viewsets.CategoryViewSet, basename='categorias')

urlpatterns = router.urls