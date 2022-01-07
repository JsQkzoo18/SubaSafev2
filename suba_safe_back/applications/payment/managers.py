from django.db import models


class PaymentManager(models.Manager):
    def users_per_payment(self, payment_id):
        query = self.filter(
            usuario_pago__id = payment_id
        )

        return query