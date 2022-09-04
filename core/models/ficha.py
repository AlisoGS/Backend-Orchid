from django.db import models
from core.models import usuario, origem, pericia, atributo


class Ficha(models.Model):
    id_ficha = models.AutoField(primary_key=True)
    user_ficha = models.ForeignKey(
        usuario.Usuario, on_delete=models.PROTECT, related_name="fichas"
    )
    orig_ficha = models.ForeignKey(
        origem.Origem, on_delete=models.PROTECT, related_name="fichas"
    )
    nome_ficha = models.CharField(max_length=255, blank=False)

    atributos = models.ManyToManyField(atributo.Atributo, related_name="fichas")
    pericias = models.ManyToManyField(
        pericia.Pericia, related_name="fichas", through="FicPer"
    )

    nex = models.PositiveIntegerField(default=0)
    vida_max = models.IntegerField(default=0)
    vida_atu = models.IntegerField(default=0)
    sani_max = models.IntegerField(default=0)
    sani_atu = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nome_ficha}"


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

    ficha = models.ForeignKey(Ficha, on_delete=models.PROTECT, related_name="FicPer")
    pericia = models.ForeignKey(
        pericia.Pericia, on_delete=models.PROTECT, related_name="PerFic"
    )
    grau_pericia = models.IntegerField(
        choices=GRAUS, null=False, blank=False, default=1
    )

    class Meta:
        unique_together = [["ficha", "pericia"]]

    def __str__(self):
        return f"{self.ficha} - {self.pericia}"
