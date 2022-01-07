from django.urls import path, include

from . import views

app_name = 'payment_app'

urlpatterns = [
    path('api/pagos/', views.PaymentListAPIView.as_view(), name='pagos'),
]