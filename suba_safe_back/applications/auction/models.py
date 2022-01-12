from django.db import models
from applications.article.models import Article
from applications.payment.models import Payment

from model_utils.models import TimeStampedModel


class Auction(TimeStampedModel):
    start = models.DateTimeField(auto_now=False)
    current_time = models.DateTimeField(auto_now=False)
    article = models.OneToOneField(Article, on_delete=models.CASCADE, related_name='articulo_subasta')
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE, blank=True, null=True, related_name='pago_subasta')
    
    class Meta:
        verbose_name = 'Subasta'
        verbose_name_plural = 'Subastas'

    def __str__(self):
        return str(self.id) + ' ' + str(self.article.name)