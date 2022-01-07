from django.db import models

from model_utils.models import TimeStampedModel


# Modelo que representa a una categoría de un artículo
class Category(TimeStampedModel):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return str(self.id) + ' ' + str(self.name) 
