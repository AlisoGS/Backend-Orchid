from media.models import Image

from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    data_nascimento = models.DateField(blank=True, null=True)

    foto = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return self.username
