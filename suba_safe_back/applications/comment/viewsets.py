# Third-Party Apps Imports
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Comment

from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, JWTAuthentication)
    permission_classes = [IsAuthenticated]

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
