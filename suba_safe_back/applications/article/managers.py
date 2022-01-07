from django.db import models


class ArticleManager(models.Manager):

    # LIstar productos por usuarios
    def articles_by_user(self, user):
        return self.filter(
            seller = user,
        )
    
    # Listar productos por categoría
    def articles_by_category(self, category):
        return self.filter(
            category = category,
        ).order_by('category')