from django.db import models
from core.models import usuario, origem


class Ficha(models.Model):
    id_ficha = models.AutoField(primary_key=True)
    user_ficha = models.ForeignKey(
        usuario.Usuario, on_delete=models.PROTECT, related_name="fichas"
    )
    orig_ficha = models.ForeignKey(
        origem.Origem, on_delete=models.PROTECT, related_name="fichas")
    nome_ficha = models.CharField(max_length=255, blank=False)
    