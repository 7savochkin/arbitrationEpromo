import uuid

from django.db import models


class PrimaryKeyMixin(models.Model):
    """Base model with primary key - uuid"""
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
