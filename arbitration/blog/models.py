from django.db import models

from arbitration.mixins.model_mixins import PrimaryKeyMixin
from tinymce.models import HTMLField


class Post(PrimaryKeyMixin):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    is_publish = models.BooleanField(default=False)
    content = HTMLField()
