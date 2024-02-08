import os.path

from django.db import models
from django.urls import reverse

from arbitration.mixins.model_mixins import PrimaryKeyMixin
from tinymce.models import HTMLField


def get_path_of_post_image(instance, filename):
    """Function for getting path for saved post image"""
    return os.path.join(f"./images/posts/{instance.slug}/{filename}")


class Post(PrimaryKeyMixin):
    """Model of Post"""
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    preview = models.ImageField(upload_to=get_path_of_post_image)
    banner = models.ImageField(upload_to=get_path_of_post_image)
    is_publish = models.BooleanField(default=False)
    content = HTMLField()

    class Meta:
        ordering = ('-created_at',)

    def get_absolute_url(self):
        """Method for getting url for post detail"""
        return reverse("blog-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title
