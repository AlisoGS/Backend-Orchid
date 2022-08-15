from django.db import models
from core.models import mod_ficha, mod_pericia


class FicPer(models.Model):
    destreinado = 1
    treinado = 2
    veterano = 3
    expert = 4
    GRAUS = [
        (destreinado, "D"),
        (treinado, "T"),
        (veterano, "V"),
        (expert, "E"),
    ]

    id_fic_per = models.ForeignKey(
        mod_ficha.Ficha, on_delete=models.PROTECT, related_name="FicPer"
    )
    id_per_fic = models.ForeignKey(
        mod_pericia.Pericia, on_delete=models.PROTECT, related_name="PerFic"
    )
    grau_pericia = models.IntegerField(choices=GRAUS, null=False, blank=False)
