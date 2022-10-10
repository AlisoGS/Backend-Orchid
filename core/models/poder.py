from django.db import models


class Poder(models.Model):
    nome = models.CharField(max_length=40, blank=False, null=False)
    desc = models.TextField(max_length=255, blank=False, null=False)

    def __str__(self):
        return f"{self.nome}"

    class Meta:
        verbose_name_plural = "Poderes"
