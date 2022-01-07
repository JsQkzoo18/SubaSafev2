from rest_framework.routers import DefaultRouter

from . import viewsets


router = DefaultRouter()

router.register(r'comentarios', viewsets.CommentViewSet, basename='comentarios')

urlpatterns = router.urls