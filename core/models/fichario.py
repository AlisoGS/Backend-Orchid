from django.db import models

from core.models import usuario


class Fichario(models.Model):
    nome = models.CharField(max_length=255, blank=False)
    dono = models.ForeignKey(
        usuario.Usuario, on_delete=models.CASCADE, related_name="Fichario"
    )
    codigo = models.CharField(max_length=20, blank=True, null=True, default=None)
    notas = models.CharField(max_length=255, blank=True, null=True)