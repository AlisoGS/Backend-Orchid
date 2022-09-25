from django.db import models

from core.models.pericia import Pericia


class Origem(models.Model):
    nome = models.CharField(default=None, max_length=50)
    desc = models.TextField(default=None, max_length=1000)
    poder = models.TextField(default=None, max_length=400)
    pericia1 = models.ForeignKey(Pericia, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    pericia2 = models.ForeignKey(Pericia, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Origens"
