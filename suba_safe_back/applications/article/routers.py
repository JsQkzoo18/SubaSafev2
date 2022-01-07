from rest_framework.routers import DefaultRouter

from . import viewsets


router = DefaultRouter()

router.register(r'articulos', viewsets.ArticleViewSet, basename='articulos')

urlpatterns = router.urls
