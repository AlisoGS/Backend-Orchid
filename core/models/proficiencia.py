from django.db import models


class Proficiencia(models.Model):
    nome = models.CharField(max_length=40, blank=False, null=False)

    def __str__(self):
        return f"{self.nome}"
