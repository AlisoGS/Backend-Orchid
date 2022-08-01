from django.db import models

class Usuario(models.Model):
    id_user = models.AutoField(primary_key=True)
    nome_user = models.CharField(max_length=255)