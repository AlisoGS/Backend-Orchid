from django.db import models

from core.models import origem, pericia, usuario
from media.models import Image


class Ficha(models.Model):
    nome = models.CharField(max_length=255, blank=False)
    foto = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None
    )
    user = models.ForeignKey(
        usuario.Usuario, on_delete=models.CASCADE, related_name="fichas"
    )
    orig = models.ForeignKey(
        origem.Origem, on_delete=models.CASCADE, related_name="fichas"
    )
    
    pericias = models.ManyToManyField(
        pericia.Pericia, related_name="fichas", through="FicPer"
    )

    nex = models.PositiveIntegerField(default=0)
    vida_max = models.IntegerField(default=0)
    vida_atu = models.IntegerField(default=0)
    sani_max = models.IntegerField(default=0)
    sani_atu = models.IntegerField(default=0)
    agili = models.SmallIntegerField(default=0)
    forca = models.SmallIntegerField(default=0)
    intel = models.SmallIntegerField(default=0)
    prese = models.SmallIntegerField(default=0)
    vigor = models.SmallIntegerField(default=0)

    def __str__(self):
        return f"{self.nome}"


class FicPer(models.Model):
    GRAUS = [
        (1, "Destreinado"),
        (2, "Treinado"),
        (3, "Veterano"),
        (4, "Expert"),
    ]

    ficha = models.ForeignKey(Ficha, on_delete=models.CASCADE, related_name="FicPer")
    pericia = models.ForeignKey(
        pericia.Pericia, on_delete=models.CASCADE, related_name="PerFic"
    )
    grau = models.IntegerField(
        choices=GRAUS, null=False, blank=False, default=1
    )

    class Meta:
        unique_together = [["ficha", "pericia"]]
        verbose_name_plural = "FichaPericias"

    def __str__(self):
        return f"{self.ficha} - {self.pericia}"

