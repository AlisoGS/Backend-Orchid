from django.db import models


class Proficiencia(models.Model):
    id_proficiancia = models.AutoField(primary_key=True)
    nome_proficiencia = models.CharField(max_length=40, blank=False, null=False)

    def __str__(self):
        return f"{self.nome_proficiencia}"
