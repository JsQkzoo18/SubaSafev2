from django.db import models


class AuctionManager(models.Manager):
    def articles_per_auction(self, auction_id):
        query = self.filter(
            articulo_subasta__id = auction_id
        )

        return query