from tabnanny import verbose
from django.db import models


class Pericia(models.Model):
    id_pericia = models.AutoField(primary_key=True)
    nome_pericia = models.CharField(max_length=40, blank=False, null=False)
    desc_pericia = models.TextField(max_length=255, blank=False, null=False)
    penalidade_carga =  models.BooleanField(default=False)
    somente_treinado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nome_pericia}"
