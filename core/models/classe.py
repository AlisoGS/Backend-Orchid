from email.policy import default

from django.db import models

from .poder import Poder
from .proficiencia import Proficiencia


class Classe(models.Model):
    nome = models.TextField(max_length=40)
    pvIni = models.IntegerField(default=0)
    pvMod = models.IntegerField(default=0)
    peIni = models.IntegerField(default=0)
    peMod = models.IntegerField(default=0)
    snIni = models.IntegerField(default=0)
    snMod = models.IntegerField(default=0)
    numpericias = models.PositiveSmallIntegerField(default=0)
    habilidade = models.ForeignKey(Poder, on_delete=models.CASCADE, related_name="+")
    habilidade2 = models.ForeignKey(Poder, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name="+")
    profi = models.ManyToManyField(Proficiencia)
    def __str__(self):
        return f"{self.nome}"