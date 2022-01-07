# Third-Party Apps
from rest_framework.generics import (
    ListAPIView,
)

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import ArticleSerializer

from .models import Article


class ListAPIViewArticleByUser(ListAPIView):
    serializer_class = ArticleSerializer

    # Idetificación y autenticación del usuario
    authentication_classes = (TokenAuthentication,)

    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        user = self.request.user
        return Article.objects.articles_by_user(user)


class ListApiViewArticleByCategory(ListAPIView):
    serializer_class = ArticleSerializer

    # # Identificación y autenticación del usuario
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        category = self.kwargs['category']
        return Article.article_objects.articles_by_category(category)


class ListApiViewArticle(ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.article_objects.all()