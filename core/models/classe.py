from django.db import models


class Classe(models.Model):
    nome = models.TextField(max_length=40)
    pvInicial = models.IntegerField(default=0)
    pvModific = models.IntegerField(default=0)
    peInicial = models.IntegerField(default=0)
    peModific = models.IntegerField(default=0)
    snInicial = models.IntegerField(default=0)
    snModific = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.nome}"