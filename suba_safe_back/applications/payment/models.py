# Imports de Django
from django.db import models
from django.conf import settings

# Imports de Modelos
#from applications.auction.models import Auction
from model_utils.models import TimeStampedModel

# Modelo que representa a un pago de un artículo
class Payment(TimeStampedModel):

    PAYMENT_TYPE_CHOICES = (
        ('0', 'TARJETA'),
        ('1', 'DEPOSITO'),
        ('2', 'CONTRAENTREGA'),
    )

    PAYMENT_STATUS_CHOICES = (
        ('0', 'Pendiente'),
        ('1', 'Pagado'),
    )

    amount = models.DecimalField('Monto', max_digits=7, decimal_places=2)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='usuario_pago')
    description = models.CharField('Descripción', max_length=130)
    payment_type = models.CharField('Tipo de Pago', max_length=25, choices=PAYMENT_TYPE_CHOICES, default=0)
    status_payment = models.CharField('Estado del Pago', max_length=25, blank=True, null=True, choices=PAYMENT_STATUS_CHOICES)
    date_payment = models.DateTimeField('Fecha de Pago', blank=True, null=True)

    class Meta:
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'

    def __str__(self):
        return 'N° [' + str(self.id) + ']' + ' ' + str(self.amount)
