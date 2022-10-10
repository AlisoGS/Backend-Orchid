from django.db import models
from core.models import ficha

class Item(models.Model):
    class Meta:
        abstract = True

    nome = models.CharField(max_length=255)
    desc = models.CharField(max_length=400, null=True, blank= True)
    espaco = models.IntegerField(default=1)
    ficha = models.ForeignKey(ficha.Ficha, on_delete=models.CASCADE, default=None)


class Arma(Item):
    num_dados = models.IntegerField(default=None)
    tipo_dado = models.IntegerField(default=None)

    def __str__(self):
        return self.nome


class Utilitario(Item):
    def __str__(self):
        return self.nome


class Vestimenta(Item):
    modificador_esq = models.IntegerField(default=None)
    modificador_pas = models.IntegerField(default=None)
    modificador_blo = models.IntegerField(default=None)

    def __str__(self):
        return self.nome
