from django.db import models
from core.models import usuario, origem, pericia, atributo


class Ficha(models.Model):
    user = models.ForeignKey(
        usuario.Usuario, on_delete=models.PROTECT, related_name="fichas"
    )
    orig = models.ForeignKey(
        origem.Origem, on_delete=models.PROTECT, related_name="fichas"
    )
    nome = models.CharField(max_length=255, blank=False)

    atributos = models.ManyToManyField(
        atributo.Atributo, related_name="fichas", through="FicAtr"
    )
    pericias = models.ManyToManyField(
        pericia.Pericia, related_name="fichas", through="FicPer"
    )

    nex = models.PositiveIntegerField(default=0)
    vida_max = models.IntegerField(default=0)
    vida_atu = models.IntegerField(default=0)
    sani_max = models.IntegerField(default=0)
    sani_atu = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nome}"


class FicPer(models.Model):
    GRAUS = [
        (1, "Destreinado"),
        (2, "Treinado"),
        (3, "Veterano"),
        (4, "Expert"),
    ]

    ficha = models.ForeignKey(Ficha, on_delete=models.PROTECT, related_name="FicPer")
    pericia = models.ForeignKey(
        pericia.Pericia, on_delete=models.PROTECT, related_name="PerFic"
    )
    grau = models.IntegerField(
        choices=GRAUS, null=False, blank=False, default=1
    )

    class Meta:
        unique_together = [["ficha", "pericia"]]
        verbose_name_plural = "FichaPericias"

    def __str__(self):
        return f"{self.ficha} - {self.pericia}"


class FicAtr(models.Model):
    ficha = models.ForeignKey(Ficha, on_delete=models.PROTECT, related_name="FicAtr")
    atributo = models.ForeignKey(
        atributo.Atributo, on_delete=models.PROTECT, related_name="FicAtr"
    )
    valor = models.SmallIntegerField()

    class Meta:
        unique_together = [["ficha", "atributo"]]
        verbose_name_plural = "FichaAtributos"

    def __str__(self):
        return f"{self.ficha} - {self.atributo}"
