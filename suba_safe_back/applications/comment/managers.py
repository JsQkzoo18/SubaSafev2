from django.db import models


class CommentManager(models.Manager):
    def users_per_comment(self, comment_id):
        query = self.filter(
            comment__id = comment_id
        )

        return query