from django.contrib.auth.models import AbstractUser
from django.db import models

from media.models import Image


class Usuario(AbstractUser):
    data_nascimento = models.DateField(blank=True, null=True, default=None)

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
