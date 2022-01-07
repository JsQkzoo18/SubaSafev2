# Third-Party Apps
from rest_framework.generics import (
    ListAPIView,
)

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Payment

from .serializers import PaymentSerializer


class PaymentListAPIView(ListAPIView):

    serializer_class = PaymentSerializer
    
    def get_queryset(self):
        return Payment.objects.all()
