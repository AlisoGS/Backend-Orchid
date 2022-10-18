from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    data_nascimento = models.DateField(blank=True, null=True, default=None)

    def __str__(self):
        return self.username
