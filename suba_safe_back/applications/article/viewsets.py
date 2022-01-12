# Third-Party Apps Imports
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


from .models import Article

from .serializers import ArticleSerializerViewSet


class ArticleViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, JWTAuthentication)
    permission_classes = [IsAuthenticated]

    serializer_class = ArticleSerializerViewSet
    queryset = Article.article_objects.all()
