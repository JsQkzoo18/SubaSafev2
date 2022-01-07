from rest_framework.generics import (
    ListAPIView,
)

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import BidSerializer

from .models import Bid


class BidAPIView(ListAPIView):
    serializer_class = BidSerializer

    def get_queryset(self):
        return Bid.objects.all()