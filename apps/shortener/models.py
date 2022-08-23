from django.db import models

SHORT_LINK_MAX_LENGTH = 50


class Link(models.Model):
    full = models.TextField()
    short = models.CharField(
        max_length=SHORT_LINK_MAX_LENGTH, unique=True, db_index=True
    )
