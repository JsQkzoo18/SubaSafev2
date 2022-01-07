# Third-Party Apps Imports
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


from .models import Article

from .serializers import ArticleSerializerViewSet


class ArticleViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    serializer_class = ArticleSerializerViewSet
    queryset = Article.article_objects.all()
