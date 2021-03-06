from django.db import models

from .services import signature_image_path


class Signature(models.Model):
    name = models.CharField(max_length=10, unique=True)
    image = models.ImageField(upload_to=signature_image_path)
    image_no_required = models.ImageField(
        upload_to=signature_image_path,
        null=True,
        blank=True,
    )
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
