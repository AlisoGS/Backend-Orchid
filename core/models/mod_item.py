from django.db import models


class Item(models.Model):
    class Meta:
        abstract = True
        verbose_name_plural = "Itens"

    id_item = models.AutoField(primary_key=True)
    nome_item = models.CharField(max_length=255)
    desc_item = models.CharField(max_length=255)
    espaco_item = models.IntegerField(default=1)


class Arma(Item):
    num_dados = models.IntegerField(default=None)
    tipo_dado = models.IntegerField(default=None)

    def __str__(self):
        return self.nome_item


class Utilitario(Item):
    def __str__(self):
        return self.nome_item


class Vestimenta(Item):
    modificador_esq = models.IntegerField(default=None)
    modificador_pas = models.IntegerField(default=None)
    modificador_blo = models.IntegerField(default=None)

    def __str__(self):
        return self.nome_item

