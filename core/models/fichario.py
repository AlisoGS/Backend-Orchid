from django.db import models
from core.models import usuario


class Fichario(models.Model):
    nome = models.CharField(max_length=255, blank=False)
    dono = models.ForeignKey(
        usuario.Usuario, on_delete=models.CASCADE, related_name="fichas"
    )