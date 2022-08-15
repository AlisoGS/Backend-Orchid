from django.db import models

class Atributo(models.Model):
    id_atributo = models.AutoField(primary_key=True)
    nome_atributo = models.CharField(max_length=25)
    