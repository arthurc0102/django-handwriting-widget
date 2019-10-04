from django.db import models

from .services import signature_image_path


class Signatures(models.Model):
    name = models.CharField(max_length=10, unique=True)
    image = models.ImageField(upload_to=signature_image_path)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
