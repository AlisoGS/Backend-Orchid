from django.db import models
from core.models import ficha, pericia


class FicPer(models.Model):
    d = 1
    t = 2
    v = 3
    e = 4
    GRAUS = [
        (d, "Destreinado"),
        (t, "Treinado"),
        (v, "Veterano"),
        (e, "Expert"),
    ]

    id_fic_per = models.ForeignKey(
        ficha.Ficha, on_delete=models.PROTECT, related_name="FicPer"
    )
    id_per_fic = models.ForeignKey(
        pericia.Pericia, on_delete=models.PROTECT, related_name="PerFic"
    )
    grau_pericia = models.IntegerField(choices=GRAUS, null=False, blank=False, default=1)
