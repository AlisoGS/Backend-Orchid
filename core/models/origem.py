from django.db import models
from core.models.pericia import Pericia


class Origem(models.Model):
    id_origem = models.AutoField(primary_key=True)
    nome_origem = models.CharField(default=None, max_length=50)
    desc_origem = models.TextField(default=None, max_length=1000)
    poder_origem = models.TextField(default=None, max_length=400)
    pericia1 = models.ForeignKey(Pericia, on_delete=models.PROTECT, related_name="+", null=True, blank=True)
    pericia2 = models.ForeignKey(Pericia, on_delete=models.PROTECT, related_name="+", null=True, blank=True)
    def __str__(self):
        return self.nome_origem

    class Meta:
        verbose_name_plural = "Origens"
