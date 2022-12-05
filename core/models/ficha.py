from email.policy import default

from django.db import models

from core.models import classe, fichario, origem, pericia, poder, trilha, usuario


class Ficha(models.Model):
    nome = models.CharField(max_length=255, blank=False)
    usuario = models.ForeignKey(
        usuario.Usuario, on_delete=models.CASCADE, related_name="fichas"
    )
    origem = models.ForeignKey(
        origem.Origem, on_delete=models.CASCADE, related_name="fichas"
    )

    fichario = models.ForeignKey(
        fichario.Fichario,
        on_delete=models.DO_NOTHING,
        related_name="fichas",
        blank=True,
        null=True,
        default=None,
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
    imagem = models.FileField(upload_to="ficha/", blank=True, null=True)
    classe = models.ForeignKey(
        classe.Classe,
        on_delete=models.CASCADE,
        related_name="fichas",
        blank=True,
        null=True,
        default=None,
    )
    trilha = models.ForeignKey(
        trilha.Trilha,
        on_delete=models.CASCADE,
        related_name="fichas",
        blank=True,
        null=True,
        default=None,
    )
    poderes = models.ManyToManyField(poder.Poder, related_name="fichas", blank=True)

    def __str__(self):
        return f"{self.nome}"


class FicPer(models.Model):
    ficha = models.ForeignKey(Ficha, on_delete=models.CASCADE, related_name="pericias")
    pericia = models.ForeignKey(
        pericia.Pericia, on_delete=models.CASCADE, related_name="PerFic"
    )

    class Meta:
        unique_together = [["ficha", "pericia"]]
        verbose_name_plural = "fichapericias"

    def __str__(self):
        return f"{self.ficha} - {self.pericia}"
