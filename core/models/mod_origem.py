from tabnanny import verbose
from django.db import models


class Origem(models.Model):
    id_origem = models.AutoField(primary_key=True)
    nome_origem = models.CharField(default=None, max_length=50)
    desc_origem = models.TextField(default=None, max_length=1000)
    poder_origem = models.TextField(default=None, max_length=400)
    
    def __str__(self):
        return self.nome_origem

    class Meta:
        verbose_name_plural = "Origens"
