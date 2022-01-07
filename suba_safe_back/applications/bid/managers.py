from django.db import models


class BidManager(models.Manager):
    def articles_per_bid(self, bid_id):
        query = self.filter(
            articulo_ofertas__id = bid_id
        )

        return query

    def bidders_per_bid(self, bid_id):
        query = self.filter(
            usuario_oferta__id = bid_id
        )

        return query