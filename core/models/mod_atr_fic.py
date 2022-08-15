from django.db import models
from core.models import mod_ficha, mod_atributo


class AtrFic(models.Model):
    id_atr_fic = models.ForeignKey(
        mod_atributo.Atributo, on_delete=models.PROTECT, related_name="atr_fic"
    )
    id_fic_atr = models.ForeignKey(
        mod_ficha.Ficha, on_delete=models.PROTECT, related_name="atr_fic"
    )
    valor = models.IntegerField(default=1, null=False, blank=False)

    def __str__(self):
        return self.id_atr_fic
