from rest_framework.generics import (
    ListAPIView,
)

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Comment

from .serializers import CommentSerializer


class CommentAPIView(ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()

