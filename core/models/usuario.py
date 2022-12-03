from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    data_nascimento = models.DateField(blank=True, null=True, default=None)
    foto = models.ImageField(upload_to="media/perfil", blank=True, null=True)

    def __str__(self):
        return self.username
