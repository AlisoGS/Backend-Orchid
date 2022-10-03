from django.db import models
from .classe import Classe

class Trilha(models.Model):
    nome = models.CharField(max_length=40, blank=False, null=False)
    desc = models.TextField(max_length=255, blank=False, null=False)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, blank=False, null=False, default=None)
    nomeNex10 = models.TextField(max_length=70, blank=False, null=False, default=None)
    descNex10 = models.TextField(max_length=600, blank=False, null=False, default=None)
    nomeNex30 = models.TextField(max_length=70, blank=False, null=False, default=None)
    descNex30 = models.TextField(max_length=600, blank=False, null=False, default=None)
    nomeNex65 = models.TextField(max_length=70, blank=False, null=False, default=None)
    descNex65 = models.TextField(max_length=600, blank=False, null=False, default=None)
    nomeNex99 = models.TextField(max_length=70, blank=False, null=False, default=None)
    descNex99 = models.TextField(max_length=600, blank=False, null=False, default=None)
    
    def __str__(self):
        return f"{self.nome}"
