from django.db import models

from models.proficiencia import Proficiencia


class Classe(models.Model):
    nome = models.TextField(max_length=40)
    pvIni = models.IntegerField(default=0)
    pvMod = models.IntegerField(default=0)
    peIni = models.IntegerField(default=0)
    peMod = models.IntegerField(default=0)
    snIni = models.IntegerField(default=0)
    snMod = models.IntegerField(default=0)
    profi = models.ManyToManyField(Proficiencia, null=True, blank=True)
    
    def __str__(self):
        return f"{self.nome}"