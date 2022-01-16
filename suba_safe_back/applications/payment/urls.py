from django.urls import path, include

from . import views, viewsets

app_name = 'payment_app'

urlpatterns = [
    path('api/pagos/', views.PaymentListAPIView.as_view(), name='pagos'),
    path('confirmar/pago/', viewsets.PaymentProcessViewSet, name='confirmar-pago'),
]